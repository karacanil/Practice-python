#16
from random import randint as ri
from random import choice as ch
import string
import time
low=string.ascii_lowercase
up=string.ascii_uppercase
num=string.digits
sym=string.punctuation
'''
Weak) 1 upper, 1 lower, 1 number, 1 symbol
Normal) 1 upper, 2 lowers , 2 numbers, 1 symbol
Strong) 2 uppers, 2 lowers, 2 numbers, 2 symbols
''' 
def showMenu():
    print('How strong you want your password to be ?')
    print('1)Strong')
    print('2)Normal')
    print('3)Weak')
    print('0)Exit')
def genPass(x):
    y=''
    poll=['1','2','3','4']
    poll2=['1','2','3','4','2','3']
    poll3=['1','2','3','4','1','2','3','4']
    if x==3:
        counter=0
        while counter!=4:
            temp=ch(poll) #1 2 3 4
            if temp=='1':
                y+=ch(up)
                poll.remove('1')
            elif temp=='2':
                y+=ch(low)
                poll.remove('2')
            elif temp=='3':
                y+=ch(num)
                poll.remove('3')
            elif temp=='4':
                y+=ch(sym)
                poll.remove('4')
            counter+=1
        return y
    if x==2:
        counter=0
        while counter!=6:
            temp=ch(poll2) #1 2 3 4
            if temp=='1':
                y+=ch(up)
                poll2.remove('1')
            elif temp=='2':
                y+=ch(low)
                poll2.remove('2')
            elif temp=='3':
                y+=ch(num)
                poll2.remove('3')
            elif temp=='4':
                y+=ch(sym)
                poll2.remove('4')
            counter+=1
        return y
    if x==1:
        counter=0
        while counter!=8:
            temp=ch(poll3) #1 2 3 4
            if temp=='1':
                y+=ch(up)
                poll3.remove('1')
            elif temp=='2':
                y+=ch(low)
                poll3.remove('2')
            elif temp=='3':
                y+=ch(num)
                poll3.remove('3')
            elif temp=='4':
                y+=ch(sym)
                poll3.remove('4')
            counter+=1
        return y                 
inp=1
while inp!=0:
    showMenu()
    inp=int(input('Select one of the options above:\n'))
    if inp==0:
        print('Bye. See you next time!')
        time.sleep(3)
    else:
        print('Here is your password:',genPass(inp))
