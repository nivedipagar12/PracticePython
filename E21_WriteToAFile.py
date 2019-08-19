'''

************* DISCLAIMER: THESE TASKS WERE POSTED ON https://www.practicepython.org ***********************************
************************* I AM ONLY PROVIDING SOLUTIONS ***************************************************************

Project/Exercise 21 : Write to a file (https://www.practicepython.org/)
                     Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play
                     with some different code, use the code from the solution), and instead of printing the results to a
                     screen, write the results to a txt file. In your code, just make up a name for the file you are saving
                     to.

                     Extras:
                     Ask the user to specify the name of the output file that will be saved.

Solution
Created on: 18/08/2019
Created by: Nivedita Pagar
'''


# Ask user for the name of the file
file_name = input("What name do you want to give to the file ? : ")

# create a new file (if one doesn't already exist) with the user provided name
file = open('%s.txt' % file_name, 'w+')

my_string = "Nivedita"

# iterate through the string
for i in range(len(my_string)):

    # and write(store in file) each letter on a new line
    file.write(my_string[i] + "\n")

# close the file
file.close()
