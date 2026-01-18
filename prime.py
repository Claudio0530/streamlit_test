"""
Este módulo proporciona funciones para calcular números primos.
"""
import math


def is_prime(n):
    """
    Determina si un número entero positivo es primo.
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def main():
    """
    Función principal que imprime los números primos menores a 100.
    """
    for i in range(100):
        if is_prime(i):
            print(i, end=' ')
    print()


if __name__ == '__main__':
    main()
