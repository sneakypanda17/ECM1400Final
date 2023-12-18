
import random
from components import initialise_board, create_battleships, place_battleships
from game_engine import attack, print_board, cli_coordinates_input, simple_game_loop

players = {}


def generate_attack(board_size, previous_attacks):
    while True:
        attack = (random.randint(0, board_size - 1), random.randint(0, board_size - 1))
        if attack not in previous_attacks:
            return attack


def ai_opponent_game_loop():
    print("Welcome to Battleship against AI!")

    # Initialize players
    players['user'] = {'board': initialise_board(), 'battleships': create_battleships()}
    players['ai'] = {'board': initialise_board(), 'battleships': create_battleships()}

    # Place battleships
    players['user']['board'] = place_battleships(players['user']['board'], players['user']['battleships'], 'custom')
    players['ai']['board'] = place_battleships(players['ai']['board'], players['ai']['battleships'], 'random')

    # Game loop
    while any(ships.values() for ships in [players['user']['battleships'], players['ai']['battleships']]):
        # User's turn
        print_board(players['ai']['board'])
        coordinates = cli_coordinates_input()
        if attack(coordinates, players['ai']['board'], players['ai']['battleships']):
            print("Hit!")
        else:
            print("Miss!")

        # AI's turn
        ai_attack = generate_attack(len(players['user']['board']))
        print(f"AI attacks at {ai_attack}")
        if attack(ai_attack, players['user']['board'], players['user']['battleships']):
            print("AI hit!")
        else:
            print("AI miss!")
        print_board(players['user']['board'])

    # Check winner
    if all(value == 0 for value in players['user']['battleships'].values()):
        print("Game over! AI wins.")
    else:
        print("Game over! You win.")

# Example usage
if __name__ == "__main__":
    ai_opponent_game_loop()
