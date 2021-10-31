"""
    Ex. 12: Scrieti un decorator pt f care sa scrie outputul lui f intr-un
    fisier, "output12.data".

    Observatii: f nu e la fel ca la ex 11.

"""


def write_output(func):
    def wrapper(a):
        file = open("output12.data", "w")
        file.write(a)
        return file.close()

    return wrapper


@write_output
def f(x):
    print(x)


f("Hello")
