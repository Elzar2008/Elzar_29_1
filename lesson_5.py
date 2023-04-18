from random import randint as generate_number, choice
import calculator as calc
from person import Person
from termcolor import cprint
import emoji
from decouple import config

print(generate_number(2, 5))
print(calc.multiplication(3, 4))

my_friend = Person('Jim', 25)
print(my_friend)

cprint("Hello, World!", "green", "on_red")
#Hi Sensei

print(emoji.emojize('Python is :thumbs_up:'))

print(config('DATABASE_URL'))
number = config('COMMENTED', default=5, cast=float)
print(number * 2)