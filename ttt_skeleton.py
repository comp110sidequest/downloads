"""Tic-tac-toe!!"""

CHARS: list[str] = ["   ", " X ", " O "]  # index 0: whitespace | index 1: X | index 2: O
BOARD = [
    [CHARS[0], CHARS[0], CHARS[0]], 
    [CHARS[0], CHARS[0], CHARS[0]], 
    [CHARS[0], CHARS[0], CHARS[0]]
] # CHARS[0] is empty, board starts completely empty

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
        # Step 1: player_name and num_turns

        # Step 2: input and indices
        player_input = input("Enter a row (0, 1, or 2) and column (0, 1, or 2), no space, for player " + player_name + ": ")
        #i: int =
        #j: int = 

        # OPTIONAL: invalid input

        # Step 3: update the board
        display_TTT()

        # Step 4: use check_win()
        num_turns += 1

        # Step 5: draw condition


def check_win(i: int, j: int) -> bool:
    """Check the row, column, and diagonal (if applicable) of the space with indices (i, j) of BOARD. Note that we do not need to check all of BOARD, just the row, column, and diagonal of the  last space."""

    # Step 6: check row

    # Step 7: check column

    # Step 8: check diagonals

    return False


def display_TTT() -> None:
    """Display the board."""
    # Step 9: display the board
    print("-------------")  # use this number of dashes - this should be printed 4 times total
    # and the string "|" should be around each character, like so: "| X | O |  |""


if __name__ == "__main__":
    main()
