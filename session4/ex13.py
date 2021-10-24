"""
    Ex. 13: Scrieti un decorator care sa modifice modul de functionare
    al functiei f. Puteti alege voi cum. Momentan, f intoarce 'cmi', un exemplu
    ar fi sa intoarca 'CmI' dupa aplicarea decoratorului.

"""


def change_f(func):
    def wrapper():
        return 'cmi'.upper()
    return wrapper


@change_f
def f():
    return 'cmi'


print(f())
