"""Tic-tac-toe!!"""

CHARS: list[str] = ["   ", " X ", " O "]  # index 0: whitespace | index 1: X | index 2: O
BOARD = [
    [CHARS[0], CHARS[0], CHARS[0]], 
    [CHARS[0], CHARS[0], CHARS[0]], 
    [CHARS[0], CHARS[0], CHARS[0]]
]  # CHARS[0] is empty, board starts completely empty

def main() -> None:
    """Entrypoint of program."""
    tic_tac_toe()

def tic_tac_toe() -> None:
    """Handling all the details of the game."""
    num_turns: int = 1  # count num_turns to know whose turn it is
    # hint: player X should move on odd turns and player O should move on even turns
    player_name: str = ""
    i: int = -1  # i and j will eventually be BOARD indices, but let's keep them at -1 for now
    j: int = -1
    display_TTT()  # display the board before we start the game
    while True:
        # Step 1
        player_name = "X" if num_turns % 2 == 1 else "O"

        # Step 2
        player_input = input("Enter a row (0, 1, or 2) and column (0, 1, or 2), no space, for player " + player_name + ": ")
        i: int = int(player_input[0])
        j: int = int(player_input[1])

        # OPTIONAL 1
        if (BOARD[i][j] != CHARS[0]):  # if this space is not empty
            print("You cannot place a token on this space!")
            continue  # restart the loop

        # Step 3
        BOARD[i][j] = CHARS[1] if player_name == "X" else CHARS[2]  # if player_name is X, put a 1 in the space; else, put a 2 there, for player_name O
        display_TTT()

        # Step 4
        if (num_turns >= 5 and check_win(i, j)):
            print("Player " + player_name + " won.")
            break
        num_turns += 1  # add 1 to the number of turns

        # Step 5
        if (num_turns == 10):
            print("Draw")
            break


def check_win(i: int, j: int) -> bool:
    """Check the row, column, and diagonal (if applicable) of the space with indices (i, j) of BOARD. Note that we do not need to check all of BOARD, just the row, column, and diagonal of the  last space."""

    # Step 6
    if (BOARD[i][0] == BOARD[i][1] and BOARD[i][1] == BOARD[i][2]):
        return True

    # Step 7
    elif (BOARD[0][j] == BOARD[1][j] and BOARD[1][j] == BOARD[2][j]):
        return True

    # Step 8
    elif ((BOARD[0][0] == BOARD[1][1] and BOARD[1][1] == BOARD[2][2]) or (BOARD[0][2] == BOARD[1][1] and BOARD[1][1] == BOARD[2][0])):  # I hard-coded the diagonal indices, which is not the best
        # please attempt to come up with a better solution than this!
        return True

    return False


def display_TTT() -> None:
    """Display the board."""
    # Step 9
    i: int = 0
    while (i < 4):
        print("-------------")  # just some dashes for appearance
        if (i < 3):
            print("|" + BOARD[i][0] + "|" + BOARD[i][1] + "|" + BOARD[i][2] + "|")  # for the i-th row, print the character in the 0th, 1st, and 2nd column
        i += 1
    # This is a little janky.
    # We can and should use a double nested loop to loop through a 2D matrix. If we use a single loop to loop through a 1D list,
    # we use a double loop, with 2 variables i and j, to loop through a 2D list. I found printing out the board rather difficult
    # with a double loop, so I did it this way. Please attempt using a double loop yourself, though!
    # Note: the same is possible for check_win()!


if __name__ == "__main__":
    main()
