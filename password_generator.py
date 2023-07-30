import random

small_letters = [chr(i) for i in range(97, 123)]
capital_letters = [chr(i) for i in range(65, 91)]
special_signs = [chr(i) for i in range(33, 48)] + [chr(i) for i in range(58, 65)] \
                + [chr(i) for i in range(91, 97)] + [chr(i) for i in range(123, 127)]
digits = [chr(i) for i in range(48, 58)]

password_length = 12
includes_small = True
includes_capital = True
includes_special = True
includes_digits = True

# includes_small, includes_capital, includes_special, includes_digits = None

def create_password(password_length, includes_small, includes_capital, includes_special, includes_digits):
    list_of_signs = []
    outcome = ''

    def conditioner(condition, list):
        if condition:
            for letter in list:
                list_of_signs.append(letter)

    conditioner(includes_small, small_letters)
    conditioner(includes_capital, capital_letters)
    conditioner(includes_special, special_signs)
    conditioner(includes_digits, digits)

    return ''.join((random.sample(list_of_signs, password_length)))


password = create_password(password_length, includes_small, includes_capital, includes_special, includes_digits)
print(password)
pass2 = create_password(10, 0, 1, 1, 1)
print(pass2)
pass3 = create_password(12, 1,1,1,1)
# parameters = 1, 1, 1, 1
# pass3 = create_password(6, parameters[0], parameters[1], parameters[2], parameters[3])
# pass4 = create_password(4, parameters[m] for m in parameters)
# print(pass3)
