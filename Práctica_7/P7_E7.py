#Escribe un programa que lea una frase (entrada por teclado), /
#y la pase como parámetro a un procedimiento./
# El procedimiento contará el número de vocales (de cada una) que aparecen, y lo imprimirá por pantalla.
def f(a):
    list1=["a","e","i","o","u","A","E","I","O","U"]
    for i in list1:
        contar=a.count(i)
        if contar==1:
            print("La vocal %s aparece %s vez."%(i,contar))
        else:
            print("La vocal %s aparece %s veces."%(i, contar))           
frase=(input("Escribe una frase: "))
f(frase)