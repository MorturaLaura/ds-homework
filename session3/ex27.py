"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa printati un strign aleator cu numarul de caractere egal
    cu numarul intreg primit.

    exemplu:
        Veti primi: 5
        Veti printa: 'ashdj' (poate fi orice alt string)
"""
import random
from string import ascii_lowercase

x = int(input())

print(''.join(random.choice(ascii_lowercase) for i in range(x)))
