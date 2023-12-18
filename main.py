import os
import json
from flask import Flask, render_template, jsonify, request

from components import initialise_board, create_battleships, place_battleships, check_game_over
from game_engine import attack, cli_coordinates_input, simple_game_loop
from mp_game_engine import generate_attack, ai_opponent_game_loop

app = Flask(__name__)

@app.route("/placement", methods=["GET", "POST"])
def placement_interface():
    # Handle GET request
    if request.method == "GET":
        return render_template(
            "placement.html", ships=player_battleships, board_size=BOARD_SIZE
        )

    # Handle POST request
    if request.method == "POST":
        data = request.get_json()
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "placement.json")
        with open(file_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)
        return jsonify({"Success": True})
    return None

ships_placed = False
@app.route("/", methods=["GET"])
@app.route("/", methods=["GET"])
def root():
    global player_board, player_battleships

    if request.method == "GET":
        player_board = initialise_board(size=BOARD_SIZE)
        try:
            with open('placement.json', 'r') as file:
                placement_data = json.load(file)

            player_board = place_battleships(player_board, player_battleships, 'custom')
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading placement data: {e}")
        players["player"]["board"] = player_board

    return render_template("main.html", player_board=player_board)

@app.route("/attack", methods=["GET"])
def process_attack():
    if request.args:
        try:
            player_list = ["player", "BOT"]
            for username in player_list:
                game_over = False
                game_over = check_game_over(username, players)
                if game_over is True:
                    winner = "BOT" if username == "player" else "PLAYER"
                    break

            if game_over is not True:
                row = request.args.get("x")
                col = request.args.get("y")
                player_attack = (int(col), int(row))
                if player_attack in player_already_attacked:
                    return "Already Attacked"
                player_already_attacked.append(player_attack)
                outcome = attack(
                    player_attack,
                    players["BOT"]["board"],
                    players["BOT"]["battleships"],
                )

                while True:
                    bot_attack = generate_attack(BOARD_SIZE)
                    if bot_attack not in bot_already_attacked:
                        break
                bot_already_attacked.append(bot_attack)
                attack(
                    bot_attack,
                    players["player"]["board"],
                    players["player"]["battleships"],
                )

            player_list = ["player", "BOT"]
            for username in player_list:
                game_over = False
                game_over = check_game_over(username, players)
                if game_over is True:
                    winner = "BOT" if username == "player" else "PLAYER"
                    break

            if game_over is True:
                if winner == "BOT":
                    return jsonify(
                        {
                            "hit": False,
                            "AI_Turn": bot_attack,
                            "finished": (f"GAME OVER {winner} WINS!"),
                        }
                    )

                return jsonify(
                    {
                        "hit": True,
                        "Player_Turn": (row, col),
                        "finished": (f"GAME OVER {winner} WINS!"),
                    }
                )
            return jsonify(
                {"hit": outcome, "Player_Turn": player_attack, "AI_Turn": bot_attack}
            )

        except UnboundLocalError:
            return "Game Over"

    return "Unknown Error"


BOARD_SIZE = 10
players = {}
bot_already_attacked = []
player_already_attacked = []

player_board = initialise_board(size=BOARD_SIZE)
bot_board = initialise_board(size=BOARD_SIZE)

player_battleships = create_battleships()
bot_battleships = create_battleships()

bot_board = place_battleships(bot_board, bot_battleships, algorithm="random")

players = {
    "player": {
        "board": player_board,
        "battleships": player_battleships,
    },
    "BOT": {
        "board": bot_board,
        "battleships": bot_battleships,
    },
}

if __name__ == "__main__":
    app.run()