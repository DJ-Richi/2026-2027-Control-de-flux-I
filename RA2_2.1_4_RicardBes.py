# Administració de Sistemes Informàtics en Xarxa
# 
# Autor: Ricard Bes Guimerà
# Data: 26/10/2026
# Versió: 1
#
# Descripció: Fes un programa que et demani un número de l’1 al 10 i segons la nota et digui: “Aprovat” o “Suspès”.
# Especificacions d'Entrada: del 1 al 10 determinar si la nota es de estar "Aprovat" o "Suspes".

nota = float(input("Introdueix un numero: "))

if nota >= 5:
    print("Estas Aprovat")
else:
    print("Estas Suspes")