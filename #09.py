#09
from random import randint
print('Welcome to the Guessing game!')
counter=1
flag=1
number=randint(1,9)
inp=''
print('I picked a number between 1 and 9 (including 1 and 9)')
while flag!=0:
    inp=input('You can enter "close" to exit or you can enter your guess:\n')
    if inp!='close':
        guess=int(inp)
        if guess==number:
            print('Bitch u guessed it. You got it right in {} guesses'.format(counter))
            print('I picked another one guess it:')
            number=randint(1,9)
        elif guess<number:
            print('You guessed too low')
            counter+=1
        elif guess>number:
            print('You guessed too high')
            counter+=1
    else:
        flag=0
