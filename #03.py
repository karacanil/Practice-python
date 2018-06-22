# 03
x=[7,4,9,85,2,1,0,6,9,13]
y=[]
for temp in x:
    if temp<5:
        y.append(temp)
print(y)
y=[]
num=int(input('Enter a number:\n'))
for k in x:
    if k<num:
        y.append(k)
print(y)
