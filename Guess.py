import random
number = random.randrange(1, 100)


guess = input('Guess a number between 1 and 100: ')
while guess != number:
    if number > guess:
        print('Think a number higher than this')
        guess = input('Guess a number between 1 and 100: ')
    else:
        print('Think a number lower than this')
        guess = input('Guess a number between 1 and 100: ')
print('Correct Guess')