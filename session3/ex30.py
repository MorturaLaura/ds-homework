"""
    Veti primi un string de la tastatura, care reprezinta o succesiune de
    paranteze rotunde, drepte si acolade. Va trebui sa spuneti daca parantezele
    sunt inchise corect, sau nu. (boolean - True|False)

    exemplu:
        Veti primi: '(([])){}'
        Veti printa: True

        Veti primi: '(()]'
        Veti printa: False
"""
x = input()

open_parentheses = ['(', '[', '{']
closed_parentheses = [')', ']', '}']
list_x = list(x)

stack = []

for i in range(len(x)):
    if x[i] in open_parentheses:
        stack.append(x[i])


