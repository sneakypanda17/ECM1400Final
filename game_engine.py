from components import initialise_board, print_board, create_battleships, place_battleships

def attack(coordinates, board, battleships):
    # Extract row and column coordinates
    row, col = coordinates

    # Get the ship at the specified coordinates
    ship = board[row][col]

    # Check if a ship is present at the coordinates
    if ship:
        # Update the board and battleships dictionary
        board[row][col] = None
        battleships[ship] -= 1

        # Check if the ship has been sunk
        if battleships[ship] == 0:
            print(f"You have sunk the {ship}!")

        return True

    return False

def cli_coordinates_input():
    while True:
        try:
            x = int(input("Enter X coordinate: "))
            y = int(input("Enter Y coordinate: "))
            return (x, y)
        except ValueError:
            print("Invalid input. Please enter numeric coordinates.")


def simple_game_loop():
    """
    Executes a simple game loop for the Battleship game.
    """
    # Print welcome message
    print("Welcome to Battleship!")

    # Initialize the game board
    board = initialise_board()

    # Create battleships
    ships = create_battleships()

    # Place battleships on the board
    board = place_battleships(board, ships)

    # Continue the game until all battleships are sunk
    while any(ships.values()):
        # Print the game board
        print_board(board)

        # Get user input for coordinates
        coordinates = cli_coordinates_input()

        # Attack the specified coordinates
        hit = attack(coordinates, board, ships)

        # Print hit or miss message
        if hit:
            print("Hit!")
        else:
            print("Miss!")

    # Print game over message
    print("Game over! You've sunk all the battleships!")

if __name__ == "__main__":
    simple_game_loop()
