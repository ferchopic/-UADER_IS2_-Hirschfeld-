#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial_OOP.py                                                        *
#* calcula el factorial de un número usando programación orientada a objetos*
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys


class Factorial:
    """Clase para calcular el factorial de un rango de números."""

    def __init__(self):
        pass

    def calcular(self, num):
        """Calcula el factorial de un número."""
        if num < 0:
            print("Factorial de un número negativo no existe")
        elif num == 0:
            return 1
        else:
            fact = 1
            while(num > 1):
                fact *= num
                num -= 1
            return fact

    def run(self, min_num, max_num):
        """Calcula los factoriales entre min_num y max_num."""
        for i in range(min_num, max_num + 1):
            print("Factorial", i, "! es", self.calcular(i))


def parse_range(rango):
    """Analiza la cadena de rango y devuelve los valores mínimo y máximo."""
    if '-' in rango:
        start, end = map(int, rango.split('-'))
        return start, end
    elif 'hasta' in rango:
        return 1, int(rango.split('hasta')[1])
    elif 'desde' in rango:
        return int(rango.split('desde')[1]), 60
    else:
        return int(rango), int(rango)


factorial_calculator = Factorial()

if len(sys.argv) == 1:
    rango = input('ingrese rango')
else:
    rango = sys.argv[1]

inicio, fin = parse_range(rango)
factorial_calculator.run(inicio, fin)
