#11
import isprime
def getint():
    return int(input('Give me number to check if it is prime or not:\n'))
#inp=int(input('Enter a number to check whether it is prime or not:\n'))
inp=getint()
if 1==isprime.prime(inp):
    print('It is a prime number')
elif 0==isprime.prime(inp):
    print('It is not a prime number')
