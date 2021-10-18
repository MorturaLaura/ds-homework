"""
    Ex. 18: Scrieti o functie care sa intoarca suma unei liste de numere
    folosind recursivitate.

    Exemplu:
        - f([1,2,3])
            ---> 6
"""


def f(list_numbers):
    if len(list_numbers) == 1:
        return list_numbers[0]
    return list_numbers[0] + f(list_numbers[1:])


print(f([1, 2, 3]))
