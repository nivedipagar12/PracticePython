'''

************* DISCLAIMER: THESE TASKS WERE POSTED ON https://www.practicepython.org************************************
************************* I AM ONLY PROVIDING SOLUTIONS ***************************************************************

Project/Exercise 4 : Divisors (https://www.practicepython.org/)
              Create a program that asks the user for a number and then prints out a list of all the divisors of that
              number. (If you don’t know what a divisor is, it is a number that divides evenly into another number.
              For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)


Solution
Created on: 12/08/2019
Created by: Nivedita Pagar
'''


# Ask for a number from the user
number = int(input("Enter a number : "))

# create an empty list for storing the divisors
divisors = []

# avoid extra loops (no number can have a divisor > its half) Ex: no divisor of 100 can be > 50
for i in range(1, int(number/2)+1):

    # append to list every time you find a divisor
    if number % i == 0:
        divisors.append(i)

# Print the list of divisors
print(str(divisors) + " are the divisors of " + str(number))


