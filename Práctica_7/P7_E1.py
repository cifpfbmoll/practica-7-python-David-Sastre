# Escribe un programa que pida un texto por pantalla,/
# este texto lo pase como parámetro a un procedimiento, y éste lo imprima/
# primero todo en minúsculas y luego todo en mayúsculas.
import os
os.system('cls')
def f (a):
    print(a.lower())
    print(a.upper())
frase=input("Escriba un texto: ")
f(frase)