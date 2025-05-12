#game
import random

def hello():
    print('welcome')
    
def roll_dice():
    return random.randint(1, 6)

def play_game():
    print("🎲 Welcome to the Dice Guessing Game!")
    while True:
        guess = input("Guess the dice roll (1-6) or type 'quit' to exit: ")
        if guess.lower() == 'quit':
            print("Thanks for playing!")
            break

        if not guess.isdigit() or not 1 <= int(guess) <= 6:
            print("Invalid input. Please enter a number from 1 to 6.")
            continue

        guess = int(guess)
        result = roll_dice()
        print(f"Dice rolled: {result}")

        if guess == result:
            print("🎉 Correct guess!")
        else:
            print("❌ Try again!")

if __name__ == "__main__":
    play_game()
