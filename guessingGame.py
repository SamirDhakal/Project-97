import random
number = random.randint(1,9)
chances = 5
while chances > 0 :
    guess = int(input("Guess a number from 1-9: "))
    chances = chances - 1
    if guess < number :
        print("Guess was to low: Guess a number higher than ", guess)

    if guess > number :
        print("Guess was to high: Guess a number lower than ", guess)

    if guess == number :
        print("You Win")
        break

    if chances <= 0 and guess != number :
        print("You Lose, The number is", number)