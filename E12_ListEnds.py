'''

************* DISCLAIMER: THESE TASKS WERE POSTED ON https://www.practicepython.org ***********************************
************************* I AM ONLY PROVIDING SOLUTIONS ***************************************************************

Project/Exercise 12 : List Ends (https://www.practicepython.org/)
                     Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new
                     list of only the first and last elements of the given list. For practice, write this code inside a
                     function.

Solution
Created on: 16/08/2019
Created by: Nivedita Pagar
'''


# Define a list
a = [5, 10, 15, 20, 25]

# Define an empty list to store the result
a_appended = []


def append_list(a):
    '''grabs the first and last element of list a and stores it in a_appended

        Parameters
        -----------
        a: list
           define list of unknown length

        Returns
        -----------
        None
        '''
    a_appended.append(a[0])
    a_appended.append(a[-1])
    print("The list generated using append() method is : " + str(a_appended))


append_list(a)



