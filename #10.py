#10
import random
list1=list(random.sample(range(1,30),12))
list2=list(random.sample(range(1,30),16))
num=[]
for i in list1:
    if i in list2 and i not in num:
        num.append(i)
print (num)
