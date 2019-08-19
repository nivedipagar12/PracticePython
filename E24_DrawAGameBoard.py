'''

************* DISCLAIMER: THESE TASKS WERE POSTED ON https://www.practicepython.org ***********************************
************************* I AM ONLY PROVIDING SOLUTIONS ***************************************************************

Project/Exercise 24 : Draw a Game Board (https://www.practicepython.org/)
                     This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 2,
                     Part 3, and Part 4.
                     Time for some fake graphics! Let’s say we want to draw game boards that look like this:

                         --- --- ---
                        |   |   |   |
                         --- --- ---
                        |   |   |   |
                         --- --- ---
                        |   |   |   |
                         --- --- ---
                     This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess,
                     19x19 for Go, and many more).
                     Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s
                     print statement.
                     Remember that in Python 3, printing to the screen is accomplished by

                     print("Thing to show on screen")
                     Hint: this requires some use of functions, as were discussed previously on this blog and elsewhere
                     on the Internet, like this TutorialsPoint link.

Solution
Created on: 19/08/2019
Created by: Nivedita Pagar
'''


def user_input():
    '''asks the user the desired size of the board

            Parameters
            -----------
            None

            Returns
            -----------
            size1
                integer representing size of the board
            '''
    global size1
    size1 = int(input("Which size board do you want ? \nPlease enter an integer for example 'n' for an 'nxn' board: "))
    return size1


def characters(size):
    '''defines the characters to be printed and the sequence in which they are to be printed

                Parameters
                -----------
                size: int
                    user defined size of the board

                Returns
                -----------
                None
                '''
    dash = "-"
    line = "|"
    space = " "
    rows = (space + 3 * dash) * size
    columns = (line + (3 * space)) * (size+1)
    for i in range(size):
        print(rows)
        print(columns)
    print(rows)


user_input()
characters(size1)
