# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 26/10/2026
# Versió: 1
#
# Descripció: Fes un programa que demani una lletra i et digui si es vocal o consonant.
# Especificacions d'Entrada: Programa que et digui si la lletra introduida es una vocal o una consonant.

lletra = str(input("Introdueix una lletra: "))

vocal = ["a","e","i","o","u"]

if (lletra == vocal [0] or lletra == vocal [1] or lletra == vocal [2] or lletra == vocal [3] or lletra == vocal [4]):
    print("Es una vocal")

else:
    print("Es una consonant")