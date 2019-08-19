'''

************* DISCLAIMER: THESE TASKS WERE POSTED ON https://www.practicepython.org ***********************************
************************* I AM ONLY PROVIDING SOLUTIONS ***************************************************************

Project/Exercise 9 : Guessing Game One (https://www.practicepython.org/)
                     Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
                     then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the
                     user input lessons from the very first exercise)

                     Extras:
                     1) Keep the game going until the user types “exit”
                     2) Keep track of how many guesses the user has taken, and when the game ends, print this out.

Solution
Created on: 16/08/2019
Created by: Nivedita Pagar
'''


import random

# Variable to control the outer while loop
continue1 = 1

# Variable to control the inner while loop
continue2 = 1

# Variable to count the number of attempts
count = 0


def generate_random_number():
    '''Generates a random number

        Parameters
        -----------
        None

        Returns
        -----------
        None
        '''
    global random_number
    random_number = random.randint(1, 9)
    print("\n**********Random number generated**********\n")


def user_guess():
    '''Decides whether the user's guess is correct or not

            Parameters
            -----------
            None

            Returns
            -----------
            None
            '''
    global count, continue2, continue1
    guess = int(input("Guess the number : "))

    # Make sure the user guesses a number between 1 and 9
    if guess < 1 or guess > 9 :
        print("Invalid input !! \nOnly choose numbers between 1 and 9")
    else:
        count += 1
        if guess == random_number:
            print("Bang On !!")
            print("You took " + str(count) + " attempts")
            continue2 = 0
        elif guess < random_number:
            print("Too Low !!")
        else:
            print("Too High !!")


def continue_playing():
    '''Asks the user whether they want to continue playing

            Parameters
            -----------
            None

            Returns
            -----------
            None
            '''
    global continue1
    continue1 = int(input("Do you want to continue playing ? Enter '1' for yes and '0' for no : "))  # You can ask for "exit"
    if continue1 == 0:
        print("\n**********Thank you for playing***********")


# Main code begins here
print("Welcome to the guessing game\nThe computer will randomly generate a number between 1 and 9\n"
      "You have to guess the number")

# Loop runs as long as the user wants to continue playing
while continue1 == 1:
    generate_random_number()
    continue2 = 1
    count = 0

    # Loop runs until the user gives correct answer
    while continue2 == 1:
        user_guess()
    continue_playing()

