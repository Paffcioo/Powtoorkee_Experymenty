import string
from random import random


def generatePassword(length, includeUpperCase = False, includeDigits = False, includePunctuation = False):
    characters = string.ascii_lowercase
    if includeUpperCase:
        characters += string.ascii_uppercase
    if includeDigits:
        characters += string.digits
    if includePunctuation:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def password(request):
    lenght = int(request.POST['length'])
    big = request.POST.get('big')
    numbers = request.POST.get('numbers')
    specials = request.POST.get('specials')
    print(lenght)
    password = generatePassword(lenght, big, numbers, specials)
    return render(request, 'password.html', {'length': password})