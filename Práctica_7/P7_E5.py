#Escribe un programa que te pida una frase y una vocal (entrada por teclado),/
#  y pase estos datos como parámetro a una función que se encargará de cambiar/
#  todas las vocales de la frase por la vocal seleccionada./
#  Devolverá la función la frase modificada, y el programa principal la imprimirá:
def f(a,b):
    x=a.replace("a", b).replace("e", b).replace("i", b).replace("o", b).replace("u", b)
    return x
frase=input("Escribe una frase: ")
vocal=input("Dame una vocal: ")
print (f(frase, vocal))