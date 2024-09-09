a=[1,2,3]
temp=[]
length=len(a)
print("length of array:",length)

for i in range(length):
    temp.append(a[i])
    #print(temp)
    if a[i]==0:
        temp.append(0)
#print(temp)
a=temp[:length]
print("After duplication:",a)
