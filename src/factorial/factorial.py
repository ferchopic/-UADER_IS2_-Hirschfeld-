#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys


def factorial(num):
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


def calcular_factoriales(rango):
    if '-' in rango:
        inicio, fin = map(int, rango.split('-'))
    else:
        inicio = int(rango)
        fin = 60 if 'hasta' in rango else 1
    for i in range(inicio, fin + 1):
        print("Factorial", i, "! es", factorial(i))


if len(sys.argv) == 1:
    rango = input("Por favor, ingrese el rango en formato 'desde-hasta', 'desde-', o '-hasta' para calcular los factoriales: ")
else:
    rango = sys.argv[1]

calcular_factoriales(rango)

''' Realice una modificación al programa para que si se omite el número como
argumento lo solicite. Pruebe. Sincronice en GitHub.'''

''' Modifique el argumento (y el ingreso manual) para aceptar números en el rango
desde-hasta (ej. 4-8) y que calcule los factoriales entre ambos extremos. Pruebe.
Sincronice en GitHub.'''

''' Modifique el argumento (y el ingreso manual) para que acepte rangos sin límite
inferior “-hasta” calculando entre 1 y el número indicado (ejemplo “-10”), lo
mismo para “desde-“ calculando entre el número indicado y 60. Tenga la
precaución de transformar las cadenas de caracteres de la especificación de
argumentos en valores enteros antes de intentar operaciones matemáticas.
Pruebe. Sincronice en GitHub.'''

'''Agregue comentarios al código generado. Pruebe. Sincronice con GitHub.'''