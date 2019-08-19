'''

************* DISCLAIMER: THESE TASKS WERE POSTED ON https://www.practicepython.org************************************
************************* I AM ONLY PROVIDING SOLUTIONS ***************************************************************

Project/Exercise 3 : List Less Than 10 (https://www.practicepython.org/)
                  Take a list, say for example this one: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
                  and write a program that prints out all the elements of the list that are less than 5.

                  Extras:
                  1) Instead of printing the elements one by one, make a new list that has all the elements less than 5
                  from this list in it and print out this new list.
                  2) Write this in one line of Python.
                  3) Ask the user for a number and return a list that contains only elements from the original list "a"
                  that are smaller than that number given by the user.

Solution
Created on: 12/08/2019
Created by: Nivedita Pagar
'''


# Define the list
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Print all elements individually
for i in range(len(a)-1):
    if a[i] < 5:
        print("Individual element: " + str(a[i]))

# Extra 1: Append the elements to a list and print the list
new_list = []
for i in range(len(a)-1):
    if a[i] < 5:
        new_list.append(a[i])
print("(EXTRA 1) List: " + str(new_list))

# Extra 2: List comprehension (Do the above things in one line)
print("(EXTRA 2) One line: " + str([i for i in a if i < 5]))

# Extra 3: User defined threshold using for loop
number = int(input("Enter the threshold for your list: "))
new_threshold_list = []
for i in range(len(a)-1):
    if a[i] < number:
        new_threshold_list.append(a[i])
print("(EXTRA 3) LOOP " + str(new_threshold_list))

# Extra 3: User defined threshold using list comprehension
print("(EXTRA 3) ONE LINE " + str([i for i in a if i < number]))

