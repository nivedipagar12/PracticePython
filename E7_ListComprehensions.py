'''

************* DISCLAIMER: THESE TASKS WERE POSTED ON https://www.practicepython.org ***********************************
************************* I AM ONLY PROVIDING SOLUTIONS ***************************************************************

Project/Exercise 7 : List Comprehensions (https://www.practicepython.org/)
                     Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
                     Write one line of Python that takes this list a and makes a new list that has only the even
                     elements of this list in it.

Solution
Created on: 14/08/2019
Created by: Nivedita Pagar
'''


# Define the list
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# create a new list with only the even elements of list a
print("The new list with even elements is = " + str([i for i in a if i % 2 == 0]))
