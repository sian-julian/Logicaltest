def valid(word):
    vowels={'a','e','i','o','u','A','E','I','O','U'}
    consonants=set('bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ')
    digit=set('0123456789')

    if len(word)< 3:
        return False

    if any(char not in (vowels|consonants|digit) for char in word):
        return False

    hasvow=any(char in vowels for char in word)
    hascons=any(char in consonants for char in word)

    return hasvow and hascons

word=input("Enter a string:")
if valid(word):
    print("true")
else:
    print("false")
