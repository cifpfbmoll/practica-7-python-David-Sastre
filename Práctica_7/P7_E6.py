#Escribe un programa que lea el nombre de una persona y un carácter/
#  (entrada por teclado), le pase estos datos a una función que /
# comprobará si dicho carácter está en su nombre. /
#El resultado de dicha función lo imprimirá el programa principal por pantalla.
def f(a,b):
    x=a.find(b)
    return x
nombre=input("Escribe un nombre: ")
letra=(input("Escribe una letra: "))
if (f(nombre, letra))<0:
    print ("No está en el nombre")
else:
    print("Está en el nombre")
