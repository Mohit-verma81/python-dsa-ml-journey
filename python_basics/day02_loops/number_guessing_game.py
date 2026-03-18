import random

secret_number = random.randint(1, 100)
attempts = 0
max_attempts = 5

print("Welcome to Number Guessing Game Created By Mohit verma")
print("Rule: You have only 5 attempt to guess number")
print("Guess a number between 1 and 100")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    if attempts >=5:
        print(f" {attempts} attempts Over. Try again....")
        break
    else:
        attempts += 1
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            break
else:
    print(f"Game Over! The correct number was {secret_number}")