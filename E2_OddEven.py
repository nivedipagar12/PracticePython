'''

************* DISCLAIMER: THESE TASKS WERE POSTED ON https://www.practicepython.org************************************
************************* I AM ONLY PROVIDING SOLUTIONS ***************************************************************

Project/Exercise 2 : Odd or Even (https://www.practicepython.org/)
                  Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate
                  message to the user. Hint: how does an even / odd number react differently when divided by 2?

                  Extras:
                  1) If the number is a multiple of 4, print out a different message.
                  2) Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
                  If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

Solution
Created on: 12/08/2019
Created by: Nivedita Pagar
'''


# Ask for user input
num = int(input("Enter the number you wish to evaluate: "))

# Main task: Differentiate odd and even
if num == 0:
    print(str(num) + " is NEITHER odd nor even (it's controversial) (MAIN TASK)")

elif num % 2 == 0:
    print(str(num) + " is an EVEN number (MAIN TASK)")

else:
    print(str(num) + " is an ODD number (MAIN TASK)")


# Extra 1: See if the result is a multiple of 4 and print a different message
if num == 0:
    print(str(num) + " divided by any number is zero (EXTRA 1)")

elif num % 4 == 0:
    print(str(num) + " is divisible by 4 (EXTRA 1)")

else:
    print(str(num) + " is not divisible by 4 (EXTRA 1)")


# Extra 2: Work with user defined numbers
number, divisor = input("Enter the number you wish to check (dividend) and the number you wish to divide it by "
                        "(divisor)").split()

# Check for loopholes
if int(number) == int(divisor) == 0:
    print(str(number) + " divided by any number is zero and anything divided by zero is infinity \nWhat are you trying "
                        "to achieve ? (EXTRA 2)")

elif int(number) == 0:
    print(str(number) + " divided by any number is zero (EXTRA 2)")

elif int(divisor) == 0:
    print("Anything divided by zero is infinity (EXTRA 2)")

# If there are no loop holes or possible divide by 0 errors, check the actual division
elif int(number) % int(divisor) == 0:
    print(str(number) + " is divisible by " + str(divisor) + " (EXTRA 2)")

else:
    print(str(number) + " is NOT divisible by " + str(divisor) + " (EXTRA 2)")

