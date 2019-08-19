'''

************* DISCLAIMER: THESE TASKS WERE POSTED ON https://www.practicepython.org ***********************************
************************* I AM ONLY PROVIDING SOLUTIONS ***************************************************************

Project/Exercise 11 : Check Primality Functions (https://www.practicepython.org/)
                     Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten,
                     a prime number is a number that has no divisors.). You can (and should!) use your answer to Exercise 4
                     to help you. Take this opportunity to practice using functions, described below.

Solution
Created on: 16/08/2019
Created by: Nivedita Pagar
'''


def is_prime(number):
    '''checks if the number is prime

            Parameters
            -----------
            number: int
                    number given by user

            Returns
            -----------
            None
            '''
    for i in range(2, int(number/2)+1):
        if number % i == 0:
            print(str(number) + " is not a prime number")
            prime = 1
            break
        else:
            prime = 0
    if prime == 0:
        print(str(number) + " is a prime number")


# Ask for a number from the user
number = int(input("Enter the number you want to test : "))
is_prime(number)


