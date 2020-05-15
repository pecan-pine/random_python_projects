import random
num = random.randint(1,101)
print('I am thinking of a number between 1 and 100. What is it? ')
guess = 0
while guess != num:
    guess = int(input())
    if guess < num:
        print('too small!')
    elif guess > num:
        print('too large!')
print('Correct! The number was', num)

