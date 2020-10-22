#!/usr/bin/env python3
# Para cambiar el limite de recursion en Python
import sys

def fibonacci_recursivo(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


# Para memorizacion se utiliza un diccionario
def fibonacci_dinamico(n, memo = {} ):
    if n == 0 or n == 1:
        return 1

    # Metodo perdir perdon y no permiso, accedemos al valor y si no se encuentra en try-except contuna el codigo
    try:
        return memo[n]
    except KeyError:
        resultado = fibonacci_dinamico(n - 1, memo) + fibonacci_dinamico(n - 2, memo)
        memo[n] = resultado
        print(memo)

        return resultado



if __name__ == '__main__':
    sys.setrecursionlimit(1002)
    n = int(input('Escoge un numero: '))
    resultado = fibonacci_dinamico(n)
    print(resultado)
