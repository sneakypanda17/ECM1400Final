<a name="readme-top"></a>
<h3 align="center">Battleships</h3>

  <p align="center">
    ECM1400-Programming Coursework
    <br />

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
    <li><a href="#license">License</a></li>
    <li><a href="#details">Details</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is the culmination of learning python and html over 3 months for ECM1400-Programming module.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* ![Python][Python-img]
* ![FLASK][FLASK-img]
* ![HTML][HTML-img]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites
Before you begin, ensure you have the following prerequisites installed:

- [Python](https://www.python.org/) 3.9.6
- [Flask](https://flask.palletsprojects.com/)
- [pytest](https://docs.pytest.org/en/stable/)

### Installation

Follow these steps to install and set up the project:

1. Clone the repository: `git clone https://github.com/sneakypanda17/NewBattleships.git`
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

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Run main.py to begin.

```bash
python main.py
```

Open a web browser and go to [http://127.0.0.1:5000/placement](http://127.0.0.1:5000/placement) to begin place your ships.
After placing your ships, wou will be redirected to the root page [http://127.0.0.1:5000](http://127.0.0.1:5000). 
The game can now begin.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Details

- **Author:** Dan Loveless
- **Source code:** [GitHub Repository](https://github.com/sneakypanda17/NewBattleships)
- **Acknowledgments:** This was the coursework project made for ECM1400-Programming at the University of Exeter

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[Python-img]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white

[HTML-img]: https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white

[FLASK-img]: https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white

