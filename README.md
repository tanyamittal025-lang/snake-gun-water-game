# Snake-Water-Gun Game (Python)

This is a simple **Snake-Water-Gun game** built using Python. It is similar to the classic **Rock-Paper-Scissors** game. The user plays against the computer, and the winner is decided based on the game rules.

## 🎮 Game Rules

* Snake drinks Water → Snake wins
* Water drowns Gun → Water wins
* Gun kills Snake → Gun wins
* If both the user and computer choose the same option, the result is a **Draw**.

##  How It Works

* The computer randomly selects **Snake, Water, or Gun** using Python's `random` module.
* The user enters their choice as:

  * `1` → Snake
  * `-1` → Water
  * `0` → Gun
* The program compares both choices and prints the result.

##  Concepts Used

* Python `random` module
* Dictionaries
* Conditional statements (`if-elif-else`)
* User input handling

##  How to Run

1. Clone this repository
2. Run the Python file:

```bash
python snake_water_gun.py
```

3. Enter your choice and play against the computer.

##  Example

```
Enter 1 for snake, -1 for water and 0 for gun: 1
You chose snake
Computer chose water
You win
```


* Play multiple rounds
* Create a graphical interface
