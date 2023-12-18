# game_engine.py
from components import initialise_board, print_board, create_battleships, place_battleships

def attack(coordinates, board, battleships):
    row, col = coordinates
    ship = board[row][col]
    if ship:
        board[row][col] = None
        battleships[ship] -= 1
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
    print("Welcome to Battleship!")
    board = initialise_board()
    ships = create_battleships()
    board = place_battleships(board, ships)

    while any(ships.values()):
        print_board(board)
        coordinates = cli_coordinates_input()
        hit = attack(coordinates, board, ships)
        if hit:
            print("Hit!")
        else:
            print("Miss!")

    print("Game over! You've sunk all the battleships!")

if __name__ == "__main__":
    simple_game_loop()
