'''

************* DISCLAIMER: THESE TASKS WERE POSTED ON https://www.practicepython.org ***********************************
************************* I AM ONLY PROVIDING SOLUTIONS ***************************************************************

Project/Exercise 25 : Guessing Game Two (https://www.practicepython.org/)
                     In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.
                     This time, we’re going to do exactly the opposite. You, the user, will have in your head a number
                     between 0 and 100. The program will guess a number, and you, the user, will say whether it is too
                     high, too low, or your number.
                     At the end of this exchange, your program should print out how many guesses it took to get your number.
                     As the writer of this program, you will have to choose how your program will strategically guess. A
                     naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you
                     hit the number. But that’s not an optimal guessing strategy. An alternate strategy might be to guess
                     50 (right in the middle of the range), and then increase / decrease by 1 as needed. After you’ve written
                     the program, try to find the optimal strategy!

Solution
Created on: 19/08/2019
Created by: Nivedita Pagar
'''


guess_one = 50
first_number = 0
last_number = 100


def user_message():
    '''prints some messages to the user

                Parameters
                -----------
                None

                Returns
                -----------
                None
                '''
    print("Welcome to the guessing game\nPlease choose an integer between 0 and 100\npsst..... Don't tell me !!!")
    print("\n\nI will try to guess the number and you have to tell me whether my guess is too high 'H', too low 'L' or "
          "correct 'C'")


def guessing_game():
    '''guesses the integer chosen by the user

                Parameters
                -----------
                None

                Returns
                -----------
                None
                '''
    user_continue = 1
    valid = 1

    # loop runs as long as user wants to play
    while user_continue == 1:

        # initial upper and lower limit
        lower_limit = 0
        upper_limit = 100

        # list to store all the guessed values to make sure there are no repetitions
        middle_list = []

        # to make sure that the middle number is an integer and not a float
        if (upper_limit + lower_limit) % 2 == 0:
            middle = int((upper_limit + lower_limit) / 2)

        # if odd number then make the answer a integer by adding 0.5
        else:
            middle = int(((upper_limit + lower_limit) / 2) + 0.5)
        correct = False

        # loop runs until the computer guesses the correct value
        while not correct:

            # make sure the user doesnt make a mistake and the pc doesn't guess a number twice
            if middle not in middle_list:
                middle_list.append(middle)
            else:
                print("Something went wrong !!\nDid you forget your number ?")
                break
            print("Guess " + str(len(middle_list)) + ": " + str(middle))
            user_answer = input("Is it correct 'C', high 'H' or low 'L' ?")
            if user_answer.upper() == 'C':
                print("The PC won !!")
                print("Number of guesses = " + str(len(middle_list)))
                break

            # set the new upper and lower limits depending on user answer high or low
            elif user_answer.upper() == 'H':
                upper_limit = middle
                if (upper_limit + lower_limit) % 2 == 0:
                    middle = int((upper_limit + lower_limit) / 2)
                else:
                    middle = int(((upper_limit + lower_limit) / 2) + 0.5)
            elif user_answer.upper() == 'L':
                lower_limit = middle
                if (upper_limit + lower_limit) % 2 == 0:
                    middle = int((upper_limit + lower_limit) / 2)
                else:
                    middle = int(((upper_limit + lower_limit) / 2) + 0.5)

            # if the user enters anything other than h, l or c
            else:
                print("\nInvalid input")
        while valid:
            try:
                user_continue = int(input("\nDo you want to continue playing ?\nEnter 1 for yes and 0 for no"))

                # if the user enters any other integer than 0 or 1, ask again
                if user_continue == 1 or user_continue == 0:
                    break
            except ValueError:
                # if the user enters a character instead of integer
                print("Only integers allowed !! ")
    print("\n**************Have a nice day !!***************")


user_message()
guessing_game()
