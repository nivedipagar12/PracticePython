'''

************* DISCLAIMER: THESE TASKS WERE POSTED ON https://www.practicepython.org ***********************************
************************* I AM ONLY PROVIDING SOLUTIONS ***************************************************************

Project/Exercise 26 : Check Tic Tac Toe (https://www.practicepython.org/)
                     This exercise is Part 2 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 1,
                     Part 3, and Part 4.

                     As you may have guessed, we are trying to build up to a full tic-tac-toe board. However, this is
                     significantly more than half an hour of coding, so we’re doing it in pieces.
                     Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe, not worrying
                     about how the moves were made.
                     If a game of Tic Tac Toe is represented as a list of lists, like so:

                     game = [[1, 2, 0],
                            [2, 1, 0],
                            [2, 1, 1]]
                     where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2
                     means that player 2 put their token in that space.
                     Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board,
                     tell me whether anyone has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a
                     row - either in a row, a column, or a diagonal. Don’t worry about the case where TWO people have won
                     - assume that in every board there will only be one winner.

                    Here are some more examples to work with:

                    winner_is_2 = [[2, 2, 0],
                        [2, 1, 0],
                        [2, 1, 1]]

                    winner_is_1 = [[1, 2, 0],
                        [2, 1, 0],
                        [2, 1, 1]]

                    winner_is_also_1 = [[0, 1, 0],
                        [2, 1, 0],
                        [2, 1, 1]]

                    no_winner = [[1, 2, 0],
                        [2, 1, 0],
                        [2, 1, 2]]

                    also_no_winner = [[1, 2, 0],
                        [2, 1, 0],
                        [2, 1, 0]]

Solution
Created on: 19/08/2019
Created by: Nivedita Pagar
'''


# define the final board after the game is finished
game = [[1, 2, 0], [2, 1, 0], [2, 1, 1]]

# specify the marker of player 1 (in real world its either x or o)
marker_player1 = 1

# specify the marker of player 2 (in real world its either x or o)
marker_player2 = 2


def win_combinations(player):
    '''checks the board for win combinations

            Parameters
            -----------
            player: int
               defines the player for whom the win combinations are being checked

            Returns
            -----------
            None
            '''

    # Split the board into three individual lists
    game0 = game[0]
    game1 = game[1]
    game2 = game[2]

    # check for all the win combinations
    if (game0[0] == game0[1] == game0[2] == player) \
            or (game1[0] == game1[1] == game1[2] == player) \
            or (game2[0] == game2[1] == game2[2] == player) \
            or (game0[0] == game1[0] == game2[0] == player) \
            or (game0[1] == game1[1] == game2[1] == player) \
            or (game0[2] == game1[2] == game2[2] == player) \
            or (game0[0] == game1[1] == game2[2] == player) \
            or (game0[2] == game1[1] == game2[0] == player):
        print(str(player) + "wins")
    else:
        print(str(player) + "Loses")


# in the actual game, you only check the win combinations for a particular player immediately after he makes a move
# and not at the end of the game, so this technique works

# pass the marker of the player you want to check for
win_combinations(marker_player1)
win_combinations(marker_player2)
