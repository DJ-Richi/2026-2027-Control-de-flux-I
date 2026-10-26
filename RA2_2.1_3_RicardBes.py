# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 26/10/2026
# Versió: 1
#
# Descripció: Fes un programa que et demani tres números i surti per pantalla el número més gran.
# Especificacions d'Entrada: Donat tres numeros et surti per pantalla el numero mes gran.

num1 = int(input("Introdueix el prinmer numero: "))
num2 = int(input("Introdueix el segon numero: "))
num3 = int(input("Introdueix el tercer numero: "))

if (num1 > num2 and num1 > num3): print("el primer numero es el mes gran.")

if (num2 > num3 and num2 > num1): print("el segon numero es el mes gran.")

if (num3 > num1 and num3 > num2): print("el tercer numero es el mes gran.")