from random import choice
import string

UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
DIGITS = string.digits
SYMBOLS = ['@', '#', '%', '*', '$', '^', '-', '?', '!']

DATA = list(UPPERCASE) + list(LOWERCASE) + list(DIGITS) + SYMBOLS

def password_generate(number, length):
    print(f"Сейчас будет сгенерировано {number} паролей длиной {length}:")
    for i in range(number):
        password = ''.join(choice(DATA) for i in range(length))
        print(password)

if __name__ == "__main__":
    number = int(input('Сколько паролей сгенерирновать?\n'))
    length = int(input('Какой длиной создать пароли? \n'))


    password_generate(number, length)
