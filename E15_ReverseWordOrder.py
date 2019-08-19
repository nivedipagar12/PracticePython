'''

************* DISCLAIMER: THESE TASKS WERE POSTED ON https://www.practicepython.org ***********************************
************************* I AM ONLY PROVIDING SOLUTIONS ***************************************************************

Project/Exercise 15 : Reverse Word Order (https://www.practicepython.org/)
                     Write a program (using functions!) that asks the user for a long string containing multiple words.
                     Print back to the user the same string, except with the words in backwards order. For example, say
                     I type the string:

                     My name is Michele

                     Then I would see the string:

                     Michele is name My

                     shown back to me.

Solution
Created on: 16/08/2019
Created by: Nivedita Pagar
'''


# Ask user to provide a string
my_string = input("Enter a String : ").split()


def reverse_words(my_string):
    '''reverses the order of string provided by user

                Parameters
                -----------
                my_string: str
                           user provided string

                Returns
                -----------
                None
                '''
    reversed_string = my_string[::-1]

    # This is an optional step to make the output look like a string and not a list
    print(" ".join(reversed_string))


reverse_words(my_string)
