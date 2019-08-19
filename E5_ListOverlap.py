'''

************* DISCLAIMER: THESE TASKS WERE POSTED ON https://www.practicepython.org ***********************************
************************* I AM ONLY PROVIDING SOLUTIONS ***************************************************************

Project/Exercise 5 : List Overlap (https://www.practicepython.org/)
                     Take two lists, say for example these two:
                     a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
                     b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
                     and write a program that returns a list that contains only the elements that are common between
                     the lists (without duplicates). Make sure your program works on two lists of different sizes.

                     Extras:
                     1) Randomly generate two lists to test this
                     2) Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll
                     get to it soon)

Solution
Created on: 13/08/2019
Created by: Nivedita Pagar
'''


import random

# Define the two lists
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# New empty list to store results
c = []

# Iterate through both the lists to find common
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            # If common is not already in the new list, add to list
            if a[i] not in c:
                c.append(a[i])
print(c)


# Extra 1: Randomly generate two lists to do this

# randomly generate length of new list a
x = random.randint(1,10)

# randomly generate length of new list b
y = random.randint(1,10)

# define two empty lists to fill with random numbers
a_new = []
b_new = []

# Add x elements to new list a
for i in range(x):
    temp_a = random.randint(1,20)
    a_new.append(temp_a)

# Add y elements to new list b
for j in range(y):
    temp_b = random.randint(1,20)
    b_new.append(temp_b)

print("The new array a = ", str(a_new))
print("The new array b = ", str(b_new))

# New empty list to store the result
d = []

# Iterate through both the new lists to find common elements
for m in range(0, len(a_new)):
    for n in range(0, len(b_new)):
        if a_new[m] == b_new[n]:
            # If common is not already in the new list, add to list
            if a_new[m] not in d:
                d.append(a_new[m])
print("The new array showing common elements between a_new and b_new is = ", str(d))

