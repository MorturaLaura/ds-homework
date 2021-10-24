"""
    Ex. 19: Scrieti o functie care primeste un string ca si parametru,
    creeaza un fisier cu numele parametrului primit (.json) si scrie in el
    un dictionar de 4 elemente aleatoare unde key = int, iar value = string,
    iar stringul sa aiba intre 3 si 6 caractere si key sa fie intre 0 si 10.

    Exemplu:
        f('ceva')
        ---> generez ceva.json ca si fisier
        ---> generez un dictionar
            {
                1: 'blabla',
                5: 'cmi',
                7: 'cmi22',
                10: 'balqef'
            }

"""
# ??? As avea o intrebare. Nu inteleg de ce, atunci cand creez dictionarul cu ajutorul for-ului de dimensiune 4 (utilizand range-ul),
# daca rulez codul de mai multe ori, cateodata dictionarul contine 2 elemente, alta data 3 elemente si alta data contine 4 elemente.
# N-ar trebui sa contina de fiecare data exact 4 element? Am incercat sa-mi dau seama utilizand debugger-ul dar n-am reusit.

import random
import string


def f(s):
    file = open(f"{s}.json", 'w')
    d = {}
    for i in range(4):
        d[int(random.choice(range(0, 11)))] = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(random.randint(3, 6)))

    file.write(str(d))
    file.close()

f('tema')
