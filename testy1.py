from utils import character_multiplier as cm

text = 'Ala ma kota i dwa psy'
print(text.split())
for word in text.split():
    print(word, len(word))
    word = word.upper()
    print(len(word))

print(text[:12:])

arr1 = [(x**2) for x in range(10,30) if (x%2==0) and (x%3==0)]

print(arr1)

print(cm(text, 5))

from password_generator import create_password as cp

hasełko = cp(20, 1, 1, 1, 1)
print(hasełko)
