import random
import json


def initialise_board(size=10):
    return [[None for _ in range(size)] for _ in range(size)]



def create_battleships(filename='battleships.txt'):
    battleships = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(':')
                if len(parts) == 2 and parts[1].isdigit():
                    battleships[parts[0]] = int(parts[1])
                else:
                    print(f"Invalid format in line: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return battleships

def place_battleships(board, ships, algorithm='simple'):
    if algorithm == 'simple':
        return place_battleships_simple(board, ships)
    elif algorithm == 'random':
        return place_battleships_random(board, ships)
    elif algorithm == 'custom':
        return place_battleships_custom(board, ships)
    else:
        print(f"Algorithm '{algorithm}' is not implemented yet.")
        return board

def place_battleships_simple(board, ships):
    row = 0
    for ship, size in ships.items():
        if row + size > len(board):
            print(f"Not enough space to place {ship}")
            break
        for col in range(size):
            board[row][col] = ship
        row += 1
    return board

def place_battleships_random(board, ships):
    for ship, size in ships.items():
        placed = False
        while not placed:
            row = random.randint(0, len(board) - 1)
            col = random.randint(0, len(board[0]) - 1)
            horizontal = random.choice([True, False])

            if can_place_ship(board, row, col, size, horizontal):
                place_ship(board, ship, row, col, size, horizontal)
                placed = True
    return board

def place_battleships_custom(board, ships):
    try:
        with open('placement.json', 'r') as file:
            placements = json.load(file)
        for ship, placement in placements.items():
            if ship in ships:
                row, col, horizontal = placement['row'], placement['col'], placement['horizontal']
                if can_place_ship(board, row, col, ships[ship], horizontal):
                    place_ship(board, ship, row, col, ships[ship], horizontal)
    except FileNotFoundError:
        print("Error: 'placement.json' file not found.")
    except json.JSONDecodeError:
        print("Error: 'placement.json' is not a valid JSON file.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return board

def can_place_ship(board, row, col, size, horizontal):
    if horizontal:
        return all(0 <= col + i < len(board[0]) and board[row][col + i] is None for i in range(size))
    else:
        return all(0 <= row + i < len(board) and board[row + i][col] is None for i in range(size))

def place_ship(board, ship, row, col, size, horizontal):
    if horizontal:
        for i in range(size):
            board[row][col + i] = ship
    else:
        for i in range(size):
            board[row + i][col] = ship

def print_board(board):
    # Print column headers
    print("  " + " ".join(str(i) for i in range(len(board[0]))))
    
    # Print each row of the board with row number
    for i, row in enumerate(board):
        print(str(i) + " " + " ".join('.' if cell is None else cell for cell in row))

def check_game_over(player, players):
    return all(size == 0 for size in players[player]["battleships"].values())


