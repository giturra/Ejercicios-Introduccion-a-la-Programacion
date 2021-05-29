# parte 1
# Definir factorial reciproco
def factorial_reciproco(n):
    i = 1
    fact = 1
    while i <= n:
        fact *= i
        i += 1
    return 1 / fact


# parte 2
def signo(n):
    if n % 2 == 0:
        return 1
    else:
        return -1


def senoaprox(x, m):
    i = 1
    acum = 0
    while i <= m:
        acum += signo(i) * x ** (2 * i - 1) * factorial_reciproco((2 * i - 1))
        i += 1
    return acum


def coseno_aprox(x, m):
    i = 1
    acum = 0
    while i <= m:
        acum += signo(i) * x ** (2 * i) * factorial_reciproco((2 * i))
        i += 1
    return acum