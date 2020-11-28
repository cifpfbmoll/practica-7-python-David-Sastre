# Escribir un programa que lea una frase, y pase ésta como parámetro/
# a una función que debe contar el número de palabras que contiene./
# Debe imprimir el programa principal el resultado. /
#Asumir que cada palabra está separada por un solo blanco.
#No se sabe cómo están separadas las palabras./
# Pueden estar separadas por más de un blanco o por signos de puntuación.
import os
os.system('cls')
def f(a):
    signos=[".",":",",",";","-",""," "]
    for i in range(len(a)):
        z=(a[i])
        for j in range (len(signos)):
            y=(signos[j])
            if z==y:
                if a([i]).isspace(a):
                    space=-1
                    a.remove(space)
                x=a.split(j)
                lista=len(x)
    listfinal=lista
    return (listfinal)
frase=input("Escribe una frase: ")
print (f(frase))


