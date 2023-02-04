# Challenge number 053: discovering palindromes using "for"
#A man a plan a canal Panama
'''frase = str(input('Say some frase: ')).strip().upper()
list = frase.split()
letters = "".join(list)
print(letters)
inverse = ''
for l in range(len(letters) - 1, -1, -1):
    inverse += letters[l]
print(inverse)
if letters == inverse:
    print('Yes, we got a PALINDROME!')
else:
    print('Sorry, we DO NOT have a PALINDROME.')'''

# NOW A BETTER SOLUTION WITHOUT "FOR"
frase = str(input('Say some frase or word: ')).strip().upper()
list = frase.split()
letters = "".join(list)
print(letters)
inverse = letters[::-1]
print(inverse)
if letters == inverse:
    print('Yes, we got a PALINDROME!')
else:
    print('Sorry, we DO NOT have a PALINDROME.')




