import random
n=int(input("Enter an integer:"))

result=set()

while(len(result)<n-1):
    result.add(random.randint(-n*2,n*2))
    
result=list(result)
result.append(-sum(result))
print(result)