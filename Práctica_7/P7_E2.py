# Escribe un programa que lea (entrada por teclado) el nombre y los dos/
# apellidos de una persona (en tres cadenas de caracteres diferentes), los pase/
# como parámetros a una función, y ésta debe unirlos y devolver una única cadena./
# La cadena final la imprimirá el programa por pantalla.
import os
os.system('cls')
def f(a,b,c):
    list1=[a,b,c]
    s=" "
    s=s.join(list1)
    return s
nombre=input("Dame un nombre: ")
apellido1=input("Dame el primer apellido: ")
apellido2=input("Dame el segundo apellido: ")
print (f(nombre, apellido1, apellido2))