'''

************* DISCLAIMER: THESE TASKS WERE POSTED ON https://www.practicepython.org ***********************************
************************* I AM ONLY PROVIDING SOLUTIONS ***************************************************************

Project/Exercise 10 : List Overlap Comprehensions (https://www.practicepython.org/)
                     This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require the
                     solution in a different way. Take two lists, say for example these two:

	                 a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	                 b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
                     and write a program that returns a list that contains only the elements that are common between the
                     lists (without duplicates). Make sure your program works on two lists of different sizes.
                     Write this in one line of Python using at least one list comprehension.
                     (Hint: Remember list comprehensions from Exercise 7).

                     The original formulation of this exercise said to write the solution using one line of Python,
                     but a few readers pointed out that this was impossible to do without using sets that I had not yet
                     discussed on the blog, so you can either choose to use the original directive and read about the
                     set command in Python 3.3, or try to implement this on your own and use at least one list comprehension
                     in the solution.

                     Extra:
                     1) Randomly generate two lists to test this

Solution
Created on: 16/08/2019
Created by: Nivedita Pagar
'''


'''I have already provided a solution for this without using sets in Exercise 5 (List Overlap), so we will use the sets 
approach'''

# Define the two lists
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# Define an empty list to store the answer
c = []

# Iterate through both the lists to find common
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            c.append(a[i])

print("This is the list of common elements with duplicates : " + str(c))
print("This is the list of common elements without duplicates using sets function : " + str(set(c)))

# Extra 1: Solution provided in Exercise 5 (List Overlap)
