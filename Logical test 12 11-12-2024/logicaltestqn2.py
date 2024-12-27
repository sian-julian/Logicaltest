arr=[]
n=int(input("Enter the size of the array:"))

for i in range(n):
    i=int(input())

    arr.append(i)

print("The array:",arr)

arr.sort()
# print(arr)
n=len(arr)
print("majority element in the array:",arr[n//2])