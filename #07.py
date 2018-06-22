#07
import random
x=random.sample(range(100),20)
y=[]
for k in x:
    if k%2==0:
        y.append(k)
print(y)
