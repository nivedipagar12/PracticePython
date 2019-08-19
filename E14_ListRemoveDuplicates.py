'''

************* DISCLAIMER: THESE TASKS WERE POSTED ON https://www.practicepython.org ***********************************
************************* I AM ONLY PROVIDING SOLUTIONS ***************************************************************

Project/Exercise 14 : List remove duplicates (https://www.practicepython.org/)
                      Write a program (function!) that takes a list and returns a new list that contains all the elements
                      of the first list minus all the duplicates.

                      Extras:
                      Write two different functions to do this - one using a loop and constructing a list, and another using sets.
                      Go back and do Exercise 5 using sets, and write the solution for that in a different function.

Solution
Created on: 16/08/2019
Created by: Nivedita Pagar
'''


# Define a list
a = [1, 1, 2, 3, 5, 8, 13, 21, 13, 34, 55, 89, 2, 5]

# Define an empty list to store the result
a_loop = []


def using_loop(a):
    '''removes duplicates from list a using a for loop

            Parameters
            -----------
            a: list
               predefined list

            Returns
            -----------
            None
            '''
    for i in range(len(a)):
        if a[i] not in a_loop:
            a_loop.append(a[i])
    print("This list was generated using loop : " + str(a_loop))


'''Function to remove duplicates from a list using sets'''


def using_sets(a):
    '''removes duplicates from list a using sets

            Parameters
            -----------
            a: list
               predefined list

            Returns
            -----------
            None
            '''
    a_sets = list(set(a))
    print("This list was generated using set() function : " + str(a_sets))


using_loop(a)
using_sets(a)
