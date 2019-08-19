'''

************* DISCLAIMER: THESE TASKS WERE POSTED ON https://www.practicepython.org ***********************************
************************* I AM ONLY PROVIDING SOLUTIONS ***************************************************************

Project/Exercise 20 : Element Search (https://www.practicepython.org/)
                     Write a function that takes an ordered list of numbers (a list where the elements are in order from
                     smallest to largest) and another number. The function decides whether or not the given number is
                     inside the list and returns (then prints) an appropriate boolean.

                     Extras:
                     Use binary search.

Solution
Created on: 18/08/2019
Created by: Nivedita Pagar
'''


# define a sorted list
my_list = [1, 2, 3, 4, 5, 6, 12, 15, 21, 30]

# define the number you want to find in the list
number = 5


def element_search(mylist, num):
    '''searches for the specified number in the list using the 'in' keyword

        Parameters
        -----------
        mylist: list
                stores the list of sorted numbers
        num: int
             stores the number that is to be searched in the list

        Returns
        -----------
        new_boolean
            boolean representing the result of search operation
        '''
    global new_boolean

    # simply find out if the given number is in the list
    new_boolean = num in mylist
    return new_boolean


def binary_search(mylistt, numb):
    '''searches for the specified number in the list using binary search

            Parameters
            -----------
            mylistt: list
                    stores the list of sorted numbers
            numb: int
                 stores the number that is to be searched in the list

            Returns
            -----------
            new_binary
                boolean representing the result of search operation
            '''
    global new_binary
    answer = False
    while not answer:
        start_index = 0
        end_index = -1

        # If the length of the list is an even number, find the mid point
        if len(mylistt)%2 == 0:
            middle = int(len(mylistt)/2)
        else:
            # If the length of the list is an odd number, find the mid point and add 0.5 to get a whole number
            middle = int((len(mylistt)/2) + 0.5)

        # check as long as the list is of size 2 or greater to avoid errors
        if len(mylistt) >= 2:

            # Find the middle number in list and compare the number with numb
            if numb == mylistt[middle]:
                new_binary = True
                break

            # If the desired number is greater than the number in the middle, only consider the second half of the list
            elif numb > mylistt[middle]:
                start_index = middle
                mylistt = mylistt[start_index:]

            # If the desired number is smaller than the number in the middle, only consider the first half of the list
            else:
                start_index = 0
                end_index = middle
                mylistt = mylistt[start_index:end_index]

        # If the length of the list is less than 2 (which means it has only one element
        # and you can directly compare the element with the desired number
        else:
            if numb in mylistt:
                new_binary = True
                break
            else:
                new_binary = False
                break
    return new_binary


element_search(my_list, number)
print("The result of boolean search is : " + str(new_boolean))
binary_search(my_list, number)
print("The result of binary search is : " + str(new_binary))
