num=input("Enter a number as String:")

i=len(num)-1
while i>=0 and num[i]=='0':
    i -= 1

if i>=0:
    print(num[:i+1])
else:
    print("0")