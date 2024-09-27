list1=[]

n=int(input("Enter the number of elements in the list:"))

for item in range(n):
    item=int(input())
    list1.append(item)

print("Original array: ",list1)

list2=list(set(sorted(item for item in list1)))

print("Sorted List: ",list2)

r=int(input("Enter the number of times the array should rotate:"))

rlist=list2[r:]+list2[:r]
print("Rotated List: ",rlist)

print("Minimum element in the list: ",min(rlist))