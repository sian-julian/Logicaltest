str1=input("Enter a String:")
vowels="aeiouAEIOU"
digits="0123456789"

vowelcnt=digitcnt=consonantcnt=0

for char in str1:
    if char in vowels:
        vowelcnt+=1
    elif char in digits:
        digitcnt+=1
    elif char.isalpha():
        consonantcnt+=1

print(f"vowel count:{vowelcnt}")
print(f"digit count:{digitcnt}")
print(f"consonant count:{consonantcnt}")