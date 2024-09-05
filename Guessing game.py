import random
def guessing_game():
    secret_number = random.randint(1, 100)
    guesses = 0
    while True:
        guesses += 1
        guess = int(input("Enter your guess (between 1 and 100): "))
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the correct number in {guesses} tries.")
            break
guessing_game()
