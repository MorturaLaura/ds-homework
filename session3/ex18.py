"""
    Veti primi un string de la tastatura.
    Veti primi doua numere intregi de la tastatura, x, y.
    Va trebui sa printati substringul de la indexul x la indexul y (inclusiv).

    exemplu:
        Veti primi: 'Center for Intelligent Machines', 2, 5
        Veti printa: 'nter'
"""
input_string = input()
x = int(input())
y = int(input())

print(input_string[x:y + 1])
