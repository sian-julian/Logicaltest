n=5

for i in range(n):
    asciiv=65
    for k in range(n-i-1):
        print(" ",end='')
    for j in range(i+1):
        print(f" {chr(asciiv)}",end='')
        asciiv+=1
    print()