#14
def delDup(x):
    y=[]
    for i in x:
        if i not in y:
            y.append(i)
    print(y)
def setDup(ex):
    ex=set(ex)
    print(ex)
l=[0,1,2,3,9,8,7,5,3,4,7,9,0,4]
setDup(l)
delDup(l)
