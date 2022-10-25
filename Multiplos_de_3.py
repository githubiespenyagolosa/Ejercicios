#!/usr/bin/env python3
"""
Autor: Nombre Apellido <nombreApellido@correo.com>
Fecha: 00/00/0000
Resumen: Programa que obtiene los números que son multiplos de 3 entre el 2 y el numero introducido
"""
numero = int(input('Introduce un numero: '))
while numero > 2:
    if numero % 3 == 0:
        print(numero)
    numero -= 1


