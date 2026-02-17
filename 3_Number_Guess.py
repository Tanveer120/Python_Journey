import random

num = random.randint(1,99)
# print(f"Int: {num}")
guess = int(input("Enter your guess: "))
count_of_guess = 1

while guess != num:
    if guess > num:
        print("Your guess is higher")
        count_of_guess = count_of_guess+1
        guess = int(input("Enter your guess: "))
    else:
        print("Your guess is lower")
        count_of_guess = count_of_guess+1
        guess = int(input("Enter your guess: "))

print(f"Congratulation! You guessed the correct number: {num}, in {count_of_guess} attempt")