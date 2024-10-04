def miss(a):
    left=min(a)
    right=max(a)
    
    # for i in a:
    #     if i>left:
    #         left=i
    
        
    # for i in a:
    #     if i<right:
    #         right=i
    
    list1=[]

    for i in range(left,right):
        if i not in a:
            list1.append(i)

    
    print("Missing numbers in the array:",list1)

a=[]
n=int(input("Enter the number of elements in the list:"))

for item in range(n):
    item=int(input())
    a.append(item)

print("Original array:",a)
miss(a)