"""
    Veti primi un string de la tastatura.
    Va trebui sa spuneti cate vocale are acest string.

    exemplu:
        Veti primi: 'cmi'
        Veti printa: 1
"""
word = input()
vowels = 'aeiouAEIOU'

x = 0
for vowel in vowels:
    x += word.count(vowel)

print("The total number of vowels are: ", x)
