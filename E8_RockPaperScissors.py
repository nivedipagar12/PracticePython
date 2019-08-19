'''

************* DISCLAIMER: THESE TASKS WERE POSTED ON https://www.practicepython.org ***********************************
************************* I AM ONLY PROVIDING SOLUTIONS ***************************************************************

Project/Exercise 8 : Rock Paper Scissors (https://www.practicepython.org/)
                     Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
                     print out a message of congratulations to the winner, and ask if the players want to start a new game)

                    Remember the rules:
                    1) Rock beats scissors
                    2) Scissors beats paper
                    3) Paper beats rock

Solution
Created on: 16/08/2019
Created by: Nivedita Pagar
'''


# Initial condition for while loop so that it runs at least once
user_continue = "y"


def ask_user_plays():
    '''Asks the two players their choice of weapon

    Parameters
    -----------
    None

    Returns
    -----------
    None
    '''
    global playerA, playerB
    print("Enter 'R' for Rock, 'P' for Paper and 'S' for Scissors")
    playerA = input("Please choose your weapon\nplayer A: ")
    playerB = input("Player B: ")


def game(playerA, playerB):
    '''Plays the game and prints the winner

    Parameters
    -----------
    playerA: str
            the weapon choice of player A
    playerB: str
            the weapon choice of player B

    Returns
    -----------
    None
    '''
    # check all the win conditions for player B
    if((playerA == "r" or playerA == "R") and (playerB == "p" or playerB == "P")) or ((playerA == "s" or playerA == "S")
            and (playerB == "r" or playerB == "R")) or ((playerA == "p" or playerA == "P") and (playerB == "s" or playerB == "S")):
        winner = "Player B"
    else:
        winner = "Player A"
    print("\n\t\tThe Winner is \n***********" + winner + "************\n")


def continue_yes_no():
    '''asks the users if they want to play more

        Parameters
        -----------
        None

        Returns
        -----------
        None
        '''
    global user_continue
    user_continue = input("Do you wish to continue playing? Enter 'y' for yes and 'n' for no : ")

    # If the user doesn't enter a valid input, stop the process
    if user_continue != "y" and user_continue != "n":
        print("Invalid Input !!!!")
        user_continue = "n"


# Main code begins here
print("\t\tWelcome to the Rock Paper Scissors Game \n\t\tRemember the rules:\n\t\t1) Rock beats scissors\n\t\t"
      "2) Scissors beat paper\n\t\t3) Paper beats rock")

# Keep playing until the users want to play
while user_continue == "y":
    ask_user_plays()
    game(playerA, playerB)
    continue_yes_no()
