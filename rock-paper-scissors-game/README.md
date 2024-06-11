# Rock Paper Scissors Game

This is a simple implementation of the classic Rock Paper Scissors game in Python. The user can play against the computer, and the game keeps track of the number of wins for both the user and the computer.

## How It Works

1. **Game Options**:
   - The game options are stored in a list: `["rock", "paper", "scissors"]`.

2. **User Input**:
   - The user is prompted to enter "rock", "paper", "scissors", or "q" to quit the game.
   - If the user input is not valid (not in the list of options), the game continues to ask for valid input.

3. **Computer Choice**:
   - The computer randomly selects an option from the list.

4. **Determine the Winner**:
   - The game compares the user's input with the computer's choice to determine the winner.
   - The game rules are:
     - Rock beats Scissors
     - Paper beats Rock
     - Scissors beat Paper
   - If both the user and the computer choose the same option, it is a tie.

5. **Score Tracking**:
   - The game keeps track of the number of wins for both the user and the computer.
   - The scores are displayed when the user decides to quit the game.

## How to Run:

1. Make sure you have Python installed on your system
2. Copy the code into a file 
3. Open a terminal and navigate to the directory containing the file
4. Run the script by executing *python file_name.py* 


## Code

```python
import random 
