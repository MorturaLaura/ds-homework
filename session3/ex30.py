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

stack = []
ok = True

parentheses = {'(': ')',
               '{': '}',
               '[': ']'}

for i in x:
    if i == '(' or i == '{' or i == '[':
        stack.append(i)
    elif i == ')' or i == '}' or i == ']':
        value = stack.pop()
        if parentheses[value] != i:
            ok = False
    else:
        continue

print(ok)



