#Escribe un programa que te pida una palabra o número, pase por parámetro/
# estos datos a una función, y ésta te diga si es o no palíndroma o capicúa./
# El programa principal imprimirá el resultado de la función:
def f(a):
    if (a)==(a[::-1]):
        x=str("La palabra es capicúa/palindroma")
        return x
    else:
        x=str("La palabra no es capicúa/palindroma")
        return x
palabra=input("Dime algo: ")
print(f(palabra))

        