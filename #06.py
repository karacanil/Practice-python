# 06
x=input('Enter a string to check if it is palindrome or not:\n')
y=''
for k in reversed(x):
    y+=k
if y.lower()==x.lower():
    print('It is palindrome')
else:
    print('It is not palindrome')
