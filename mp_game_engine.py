import random
from components import initialise_board, create_battleships, place_battleships
from game_engine import attack, print_board, cli_coordinates_input, simple_game_loop

players = {}


def generate_attack(board_size=10):
    # Generate random attack coordinates within the board size
    return (random.randint(0, board_size - 1), random.randint(0, board_size - 1))


def ai_opponent_game_loop():
    # Game loop for playing against AI opponent
    print("Welcome to Battleship against AI!")

    # Initialize player boards and battleships
    players['user'] = {'board': initialise_board(), 'battleships': create_battleships()}
    players['ai'] = {'board': initialise_board(), 'battleships': create_battleships()}

    # Place battleships on player boards
    players['user']['board'] = place_battleships(players['user']['board'], players['user']['battleships'], 'custom')
    players['ai']['board'] = place_battleships(players['ai']['board'], players['ai']['battleships'], 'random')

    while any(ships.values() for ships in [players['user']['battleships'], players['ai']['battleships']]):
        # Print AI's board
        print_board(players['ai']['board'])

        # Get user's attack coordinates from command line input
        coordinates = cli_coordinates_input()

        # Perform attack on AI's board
        if attack(coordinates, players['ai']['board'], players['ai']['battleships']):
            print("Hit!")
        else:
            print("Miss!")

        # Generate AI's attack coordinates
        ai_attack = generate_attack(len(players['user']['board']))
        print(f"AI attacks at {ai_attack}")

        # Perform attack on user's board
        if attack(ai_attack, players['user']['board'], players['user']['battleships']):
            print("AI hit!")
        else:
            print("AI miss!")

        # Print user's board
        print_board(players['user']['board'])

    if all(value == 0 for value in players['user']['battleships'].values()):
        print("Game over! AI wins.")
    else:
        print("Game over! You win.")