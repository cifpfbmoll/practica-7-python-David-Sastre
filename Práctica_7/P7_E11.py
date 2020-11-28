#Escribe un programa que te pida una frase, y pase la frase como parámetro a una función./
# Ésta debe devolver si es palíndroma o no, y el programa principal escribirá el resultado por pantalla:
import os
os.system('cls')
def f(a):
    x=frase.replace(" ","")
    if (x)==(x[::-1]):
        b=(f"{frase}, la frase es palindroma")
        return b
    else:
        b=(f"{frase}, la frase no es palindroma")
        return b
frase=input("Dime algo: ")
print(f(frase))