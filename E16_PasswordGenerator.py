'''

************* DISCLAIMER: THESE TASKS WERE POSTED ON https://www.practicepython.org ***********************************
************************* I AM ONLY PROVIDING SOLUTIONS ***************************************************************

Project/Exercise 16 : Password Generator (https://www.practicepython.org/)
                     Write a password generator in Python. Be creative with how you generate passwords - strong passwords
                     have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random,
                     generating a new password every time the user asks for a new password. Include your run-time code in a
                     main method.

                     Extra:

                     Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a
                     list.

Solution
Created on: 17/08/2019
Created by: Nivedita Pagar
'''


import string
import random


# Import all lower case letters
lower_case_letters = string.ascii_lowercase

# Import all the upper case letters
upper_case_letters = string.ascii_uppercase

# Import all the digits
digits = string.digits

# Import all the punctuations
punctuations = string.punctuation

# The program runs as long as the user wants to generate new passwords
user_continue = 1

# while loop variables
valid = 0
valid2 = 0
valid3 = 0


def character_order(length):
    '''generates a random order for characters in case of a strong password

    Parameters
    -----------
    length: int
            user provided length of password

    Returns
    -----------
    None
    '''
    global new_order

    # create an empty list to store the random order of characters
    new_order = []

    # define a list of characters to choose from
    list_all = ["lower_case_letters", "upper_case_letters", "digits", "punctuations"]
    for i in range(length):
        new_order.append(random.choice(list_all))


def weak_password(length):
    '''generates a weak password of desired length

                        Parameters
                        -----------
                        length: int
                                user provided length of password

                        Returns
                        -----------
                        None
                        '''
    password_weak = ""
    for i in range(length):
        # in case of a weak password, only generate a word with all lower case letters
        password_weak += random.choice(lower_case_letters)
    print("This is a randomly generated weak password of desired length: " + password_weak)


def medium_password(length):
    '''generates a password with medium complexity of desired length

                            Parameters
                            -----------
                            length: int
                                    user provided length of password

                            Returns
                            -----------
                            None
                            '''
    password_medium = ""

    # In case of an even number, there will be alternate lower case letters and digits
    if length%2 == 0:
        for i in range(int(length/2)):
            password_medium += random.choice(lower_case_letters) + random.choice(digits)
    else:
        # In case of odd number, there will be alternate lower case letters and digits
        for i in range(int(length/2)):
            password_medium += random.choice(lower_case_letters) + random.choice(digits)
        # And there will be one additional digit to reach the desired length
        password_medium += random.choice(digits)
    print("This is a randomly generated medium password of desired length: " + password_medium)


def strong_password(new_order):
    '''generates a strong password of desired length with the new randomly generated order of characters

                                Parameters
                                -----------
                                new_order: list
                                           list that holds the new randomly generated order of characters

                                Returns
                                -----------
                                None
                                '''
    global password_strong
    password_strong = ""

    # Password is generated according to the new order of characters set in character_order()
    for i in range(len(new_order)):
        # The elements are appended depending on the order specified in new_order[]
        if new_order[i] == "lower_case_letters":
            password_strong += random.choice(lower_case_letters)
        elif new_order[i] == "upper_case_letters":
            password_strong += random.choice(upper_case_letters)
        elif new_order[i] == "digits":
            password_strong += random.choice(digits)
        else:
            password_strong += random.choice(punctuations)
    print("This is a randomly generated strong password of desired length: " + password_strong)


def main():
    '''calls the necessary functions to generate a random password of desired length and complexity

                                    Parameters
                                    -----------
                                    None

                                    Returns
                                    -----------
                                    None
                                    '''
    global valid, valid2

    # Loop runs as long as the user doesn't provide a valid input
    while valid == 0:
        try:
            # Ask user for their desired length
            length = int(input("Enter your desired length of password : "))

        # Handle the value error raised if the user inputs a string
        except ValueError:
            print("Invalid Input !! Only integers allowed !!")
        else:
            # If no error is raised, we break out of the while loop and go to next statement
            break

    # Loop runs as long as the user doesn't provide a valid input
    while valid2 == 0:
        weak_strong = input("Do you want your password to be strong, medium or weak ?\nEnter 's' for strong, 'm' for "
                        "medium and 'w' for weak:")
        if weak_strong.lower() == "w":
            weak_password(length)
            # break out of the loop once you get a valid input ("w", "m" or "s")
            break
        elif weak_strong.lower() == "m":
            medium_password(length)
            break
        elif weak_strong.lower() == "s":
            character_order(length)
            strong_password(new_order)
            break
        else:
            # continue the loop if you get anything other than "w", "m" or "s"
            print("Invalid input !!")


print("Welcome to the random password generator")

# You can also use while user_continue: if you're sure that the user will input either 0 or 1
# but here I'm accounting for typos/human error
while user_continue == 1:
    main()

    # Loop runs as long as the user doesn't provide a valid input
    while valid3 == 0:
        try:
            user_continue = int(input("Do you want to generate more passwords ? Enter 1 for yes and 0 for no : "))
            if user_continue == 0 or user_continue == 1:
                # break out of the loop if you get either 1 or 0
                break
            else:
                # print this message if you get any other integer
                print("Invalid Input !! Only '0' and '1' allowed !!")
        # print this message if you get a string input
        except ValueError:
            print("Invalid Input !! Only integers allowed !!")


