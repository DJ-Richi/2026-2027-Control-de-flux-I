# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 26/10/2026
# Versió: 1
#
# Descripció: Fes un programa que donat un número et digui si és parell o imparell.
# Especificacions d'Entrada: Donat un numero et digui si es par o senar.

num1 = int(input("Introdueix un numero: "))

if num1 % 2 == 0:
    print("El numero es parell")
else:
    print("El numero es senar")