[<img src="https://travis-ci.org/seanchon/simple_terminal.svg?branch=master">](https://travis-ci.org/seanchon/simple_terminal)
[<img src="https://img.shields.io/pypi/pyversions/simple-terminal.svg">](https://pypi.python.org/pypi/simple_terminal)

# simple_terminal
A simple way to run terminal commands within a Python script.


## Code Example
```python
from simple_terminal import Terminal

terminal = Terminal()

results = terminal.command('ls')
```

## Motivation
This library exists to run terminal commands from within a script to create easier automation of commonly performed tasks.

## Installation
pip install simple_terminal

## License
MIT
