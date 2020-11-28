#Escribe un programa que lea (entrada por teclado) una frase/
# y la pase como parámetro a un procedimiento, y éste debe mostrar la frase/
# con un carácter en cada línea.
import os
os.system('cls')
def f(a):
    for i in range (len(a)):
        print (a[i])
frase=input("Escribe una frase: ")
f(frase)