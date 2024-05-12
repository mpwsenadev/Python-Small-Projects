import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to Guess the Number!")
    print("Try to guess the number between 1 and 100.")

    while True:
        guess = int(input("Enter your guess: "))

        attempts += 1

        if guess < number_to_guess:
            print("Higher!")
        elif guess > number_to_guess:
            print("Lower!")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts!")
            break

def main():
    guess_the_number()

if __name__ == "__main__":
    main()
