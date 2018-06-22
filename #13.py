#13
inp=int(input('How many fibonnaci numbers you want me to generate:\n'))
def fibonnaci(num):
    counter=0
    x=1
    y=0
    while counter<num:
        print(x)
        temp=x
        x+=y
        y=temp
        counter+=1
fibonnaci(inp)
