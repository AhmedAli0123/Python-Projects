# Simple Number Guessing Game 🎮

This is a basic **number guessing game** created in Python using Jupyter Notebook (`.ipynb`).  

## How It Works:
- The computer selects a **random number** between 1 and 3.
- The user has to **guess the number**.
- If the guess is **correct**, the game ends with a success message. 🎉
- If the guess is **wrong**, the game asks the user to **try again** until they guess correctly.

## Code Example:
```python
import random

secret_num = random.randint(1, 3)

while True:
    guess_num = int(input("Guess the number between 1-3: "))

    if guess_num == secret_num:
        print("You guessed the right number! 🎉")
        break
    else:
        print("Wrong guess! Try again.")
