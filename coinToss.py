import random

def converting(guessss):
    if guessss == 'heads':
        guessss = 1
        return guessss
    if guessss == 'tails':
        guessss = 0
        return guessss

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
guess = converting(guess)
toss = random.randint(0, 1) # 0 is tails, 1 is heads

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    guess = converting(guesss)
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
