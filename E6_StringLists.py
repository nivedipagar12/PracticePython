'''

************* DISCLAIMER: THESE TASKS WERE POSTED ON https://www.practicepython.org ***********************************
************************* I AM ONLY PROVIDING SOLUTIONS ***************************************************************

Project/Exercise 6 : String Lists (https://www.practicepython.org/)
                     Ask the user for a string and print out whether this string is a palindrome or not.
                     (A palindrome is a string that reads the same forwards and backwards.)

Solution
Created on: 13/08/2019
Created by: Nivedita Pagar
'''


# Ask user for a string
my_string = input("Enter a string : ")

# Check if the string is equal to its reverse
if my_string == my_string[::-1]:
    print(my_string + " is a Palindrome")
else:
    print(my_string + " is not a Palindrome")

