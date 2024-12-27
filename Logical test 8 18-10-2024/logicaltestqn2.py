def str_reverse(str1):
    print(str1[::-1])

str1=[]
n=int(input("Enter the number of characters in the String:"))

for item in range(n):
    item=input()
    str1.append(item)

print("Original String:",str1)
str_reverse(str1)