def character_multiplier(character, multiplier):
    return character*multiplier

# print(character_multiplier('a', 10))
# b = 'fg'
# print(character_multiplier(b, 10))

def mnożenie_przez_pi(liczba):
    from math import pi
    return pi*int(liczba)

coś = [2, 3, 4]
def foo1(*arg):
    return mnożenie_przez_pi(arg)

print(foo1(coś))
