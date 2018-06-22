#18
import random
import time

def cowbull(n,g):
    cow=0
    bull=0
    for each in n:
        for element in g:
            if each==element:
                if n.index(each)==g.index(element):
                    cow+=1
                else:
                    bull+=1
    if g!=n:
        print('{}cow(s) and {}bull(s)\n'.format(cow,bull))

print('''
Let's play a game of Cowbull!
I will generate a random 4-digit number and you have to guess the number
For every correct digit in the correct place you get a cow,
For every correct digit in the wrong place you get a bull
I hope we're ready to go
''')

flag=''
while flag!='n':
    guess=''
    flag=input('Ready to play guess game ?\n(Y)es or (N)o:')
    if flag.lower()=='y':
        number=str(random.randint(1000,9999))
        print('\nA random 4-digit number generated')
        while guess!=number:
            guess=str(input('Enter your guess:'))
            cowbull(number,guess)
        print('Wow! You guessed it')
    else:
        print('See you next time!')
time.sleep(3)

