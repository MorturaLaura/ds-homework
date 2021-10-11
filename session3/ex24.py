"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa spuneti daca acel numar este palindrom, folosind tipul de date
    boolean (True, False)

    Observatii:
        - palindrom: numarul este acelasi de la stranga la dreapta,
        si de la dreapta la stanga

    exemplu:
        Veti primi: 12321
        Veti printa: True

        Veti primi: 1232
        Veti printa: False
"""
x = int(input())

# O modalitate ar fi schimband tipul de date din numar intreg in string
"""
y = str(x)
if y == y[::-1]:
    print(True)
else:
    print(False)
"""

#O alta modalitate ar fi determinand inversul numarului intreg primit de la tastatura
x_for_reverse = x
y = 0
while x_for_reverse != 0:
    y = y*10 + x_for_reverse % 10
    x_for_reverse = int(x_for_reverse/10)

if y == x:
    print(True)
else:
    print(False)

