import random
import art
print(art.logoo)
print("Welcome to the Number Guessing Project")
print("I am thinking of a number between 1 and 100")
difficulty = input("CHOOSE difficulty, 'easy' or 'hard'?")
attempt = 0
if difficulty == "easy":
    attempt = 10
else:
    attempt = 5
random_number = random.randint(1,100)
guess = int(input("Guess a number between 1 and 100"))
while attempt > 0:
    if guess == random_number:
        print(f'You guessed the number {random_number} in {attempt} attempts remaining')
        attempt = 0

    elif guess > random_number:
        print("Too high")
        attempt -= 1
    elif guess < random_number:
        print("Too low")
        attempt -= 1
    guess = int(input(f" You Have {attempt} attempts left to guess the number\nhadMake a guess:"))
print("heheheheh\nLoser come again later\nThank you for playing")