# We are going to write a program that generates a random number and asks the user to
# guess it.
# If the player’s guess is higher than the actual number, the program displays “Lower
# number please”. Similarly, if the user’s guess is too low, the program prints “higher
# number please” When the user guesses the correct number, the program displays the
# number of guesses the player used to arrive at the number.
# Hint: Use the random module.

import random

n = random.randint(1, 100)
a = -1
guesses = 0

print("You have to guess the number between 1 to 100")

while a != n:
    a = int(input("Guess the number : "))
    guesses += 1

    if a > n:
        print("Lower number please")
    elif a < n:
        print("Higher number please")

print(f"You have guessed the number {n} correctly in {guesses} attempts")

if guesses == 1:
    print("Brilliant guess!")
elif guesses <= 5:
    print("Excellent guess!")
elif guesses <= 10:
    print("Good guess!")
elif guesses <= 15:
    print("Can do better...")
else:
    print("Bad guessing")