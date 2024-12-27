s=input("Enter a String:")
vowel=['a','e','i','o','u','A','E','I','O','U']
res=""

for char in s:
    if char not in vowel:
        res=res+char

print("String without any vowels:",res)