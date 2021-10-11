"""
    Veti primi un string de la tastatura.
    Va trebui sa printati numarul de vocale si numarul de consoane din
    acel string.

    exemplu:
        Veti primi: 'center'
        Veti printa:
        2 (pentru vocale)
        4 (pentru consoane)
"""
x = input()
vowels = 'aeiouAEIOU'

# Un mod ar fi prin a trasnforma stringul intr-o lista si a numara fiecare consoana si vocala
"""
l1 = list(x)
nb_vowels = 0
nb_consonant = 0

for i in l1:
    if i in vowel:
        nb_vowels += 1
    else:
        nb_consonant += 1
    

print(nb_vowels, '\n', nb_consonant)
"""

# O alta modalitate ar fi prin a identifica numarul total de vocale, iar apoi a scodea valoarea acestora din
# dimensiunea stringului pentru a afla numarul consoanelor din string

count_vowels = 0
for vowel in vowels:
    if vowel in x:
        count_vowels += x.count(vowel)

count_consonant = len(x) - count_vowels
print(count_vowels, '\n', count_consonant)