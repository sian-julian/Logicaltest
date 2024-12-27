str1=input("Enter the fisrt string:")
str2=input("Enter the second string:")

str1=str1.lower()
str2=str2.lower()
if sorted(str1)==sorted(str2):
    print("They are anagram")
else:
    print("Not Anagram")