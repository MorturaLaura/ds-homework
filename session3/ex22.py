"""
    Veti primi un string de la tastatura.
    Va trebui sa afisati acel string cu o litera mare/una mica.

    exemplu:
        Veti primi: 'center'
        Veti printa: 'CeNtEr'
"""

x = input()
x = list(x)

for i in range(len(x)):
    if i % 2 == 0:
        x[i] = x[i].upper()

x = ''.join(x)
print(x)
