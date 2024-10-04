def unique(s1):
    n=len(s1)
    for i in range(n):
        found=True

        for j in range(n):
            if i!=j and s1[i]==s1[j]:
                found=False
                break
            
        if found==True:
            return i
        
    return -1
        
s1=input("Enter a string:")

print(unique(s1))