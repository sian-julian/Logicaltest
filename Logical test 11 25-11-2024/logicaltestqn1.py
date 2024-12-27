num=input("Enter a number:")

res=""
for char in num:
    if '0'<=char<='9':
        res=res+char
    
print("number without non-numeric characters:",res)