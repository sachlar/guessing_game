# intro
import random

def simple_number_game():
    print("Welcome to my simple number guessing game.")
    print("I'm thinking of a number between 1 & 100. Guess which number I am thinking of?")

    my_number = random.randint(1, 100)
    number_of_guesses = 0

    while True:
        try:
            guess = int(input("Guess my number: "))
            number_of_guesses += 1

            if guess < my_number:
                print("Too low, try again.")
            elif guess > my_number:
                print("Too high, try again")        
            else:
                print(f"Congratulations, you guessed my number in {number_of_guesses} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

simple_number_game()


