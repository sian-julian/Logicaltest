def common(str1,str2):
    for char in str1:
        if char in str2:
            print("common characters found")
            return
    print("no common characters found")
    return

str1=input("Enter the fisrt string:")
str2=input("Enter the second string:")

str1=str1.lower()
str2=str2.lower()

common(str1,str2)


