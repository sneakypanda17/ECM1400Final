<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>




# Battleships

## Description

The Battleship game is a strategic guessing game typically played by two players. In the traditional board game, each player has a board with a grid of squares, typically 10x10, where they can place a fleet of ships without the opponent's knowledge. The objective is to sink your opponent's fleet before they sink yours. Each player takes turns to declare coordinates for their strike and the opponent replies whether that is a hit or miss until one player has no battleships remaining. 

This project is a web based flask implememtation of a single player vs AI version of this popular game.

## Prerequisites

The following must be installed.

- [Python](https://www.python.org/) 3.9.6
- [Flask](https://flask.palletsprojects.com/)
- [pytest](https://docs.pytest.org/en/stable/)

You can install these dependencies using the following commands:

## Install Python 3.9.6

## For Windows

Visit [Python Downloads](https://www.python.org/downloads/release/python-396/) and download the installer. Follow the installation instructions.

## For macOS

Open a terminal and run:

```bash
brew install python@3.9.
```

## For Linux(Debian/Ubuntu)

Open a terminal and run:

```bash
sudo apt-get update
sudo apt-get install python3.9
```

## Install Flask and pytest

```bash
pip install flask
pip install pytest
```

Make sure to have Python and pip installed on your system before executing the commands.

## Installation

Follow these steps to install and set up the project:

1. Clone the repository: `git clone https://github.com/W3r5l3y/ECM1400-Battleships-Coursework.git`
2. Navigate to the project directory: `cd battleships`
3. Install the project using the `setup.py` file:

```bash
python setup.py install
```

Alternatively, you can test the package by installing it from Test PyPI. First, create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
```

Then, install the package from Test PyPI:

```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ battleships-pgk-jworley==0.0.1
```

Now you can use the package in your virtual environment.

## Getting Started

Run the main module to start the web server:

```bash
python main.py
```

Open your web browser and go to [http://127.0.0.1:5000/placement](http://127.0.0.1:5000/placement) to begin placing your ships on a grid.
After successfully placing your fleet and submitting the grid, you will be redirected to the root page [http://127.0.0.1:5000](http://127.0.0.1:5000). From there, you can initiate attacks on your opponent's grid until either you or the opponent emerges victorious in the game.

## Testing

To run the tests for the project, you can use the following commands for different testing modules:

### Test Components

Run this command to test the individual components of the Battleships project.

```bash
pytest test_components.py
```

Execute this command to ensure the overall functionality of the Battleships project.

```bash
pytest test_functionality.py
```

Use this command to run tests for the helper functions utilized in the Battleships project.

```bash
pytest test_helper_functions.py
```

Run this command to check the specific functionality related to student implementations.

```bash
pytest test_students.py
```

## Developer Documentation

The program is organized into four distinct modules:

- **components.py:** This module houses functions responsible for initializing either a `simple_game_loop` or an `ai_opponent_game_loop`, including tasks like board initialization and battleship placement.

- **game_engine.py:** Functions crucial for the gameplay mechanics of a `simple_game_loop` are stored in this module. This includes operations like receiving coordinate inputs from the user and executing attacks on the board.

- **mp_game_engine.py:** Dedicated to the mechanics of an `ai_opponent_game_loop`, this module encompasses additional functions. These functions involve tasks such as displaying the user's board and generating AI attacks that target the user's board.

- **main.py:** The main module orchestrates the integration of functions from the preceding modules using a Flask web interface. This integration results in the creation of an online Battleships game, providing an interactive and engaging platform for players.

## License

This project is licensed under the [MIT License](LICENSE.txt). See the [LICENSE.txt](LICENSE.txt) file for more details.

### Details

- **Author:** James Worley
- **Source code:** [GitHub Repository](https://github.com/W3r5l3y/ECM1400-Battleships-Coursework)
- **PyPI:** [Package on PyPI](https://test.pypi.org/project/battleships-pgk-jworley/0.0.2/)
- **Acknowledgments:** This was the coursework project made for ECM1400 at Exeter University