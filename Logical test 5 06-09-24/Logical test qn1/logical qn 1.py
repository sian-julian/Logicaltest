a=[]
n=int(input("Enter the no of elements in the list:"))
print("Elements in the list")
for i in range(n):
    item=int(input())
    a.append(item)
print("The List:",a)

unique=sorted(p for p in a if a.count(p)==1)

if not unique:
    print("null")
else:
    print("largest no in unique list:",unique[-1])
