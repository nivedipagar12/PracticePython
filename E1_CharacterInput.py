'''

************* DISCLAIMER: THESE TASKS WERE POSTED ON https://www.practicepython.org************************************
************************* I AM ONLY PROVIDING SOLUTIONS ***************************************************************

Project/Exercise 1 : Character Input (https://www.practicepython.org/)
              Create a program that asks the user to enter their name and their age. Print out a message addressed to
              them that tells them the year that they will turn 100 years old.

              Extras:
              1) Add on to the previous program by asking the user for another number and printing out that many
              copies of the previous message. (Hint: order of operations exists in Python)
              2) Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same
              as pressing the ENTER button)

Solution
Created on: 12/08/2019
Created by: Nivedita Pagar
'''


# Import datetime package to determine the current year instead of hard coding it.
import datetime


# User variables
name, age = input("Enter your name and age (separated by a space): ").split()
# Create a datetime object
now = datetime.datetime.now()
# Find out the current year, subtract the current age from 100 and add the difference to the current year
current_year = now.year + (100 - int(age))
num = int(input("Enter the number of times you wish to see the result : "))


# Simply print the result
print("You will turn 100 in the year : " + str(current_year))


# Print the result "num" times using a for loop
for i in range(0, num):
    print("(EXTRA LOOP) You will turn 100 in the year : " + str(current_year))


# Print the result "num" times by manipulating strings
print(("(EXTRA STRING MANIPULATION) You will turn 100 in the year : " + str(current_year) + "\n") * num)

