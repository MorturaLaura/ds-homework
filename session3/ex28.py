"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa printati suma numerelor pana la numarul respectiv.

    exemplu:
        Veti primi: 5
        Veti printa: 15
"""
x = int(input())

result = 0
for i in range(1, x + 1):
    result += i

print(result)
