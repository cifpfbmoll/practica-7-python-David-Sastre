#Escribe un programa que le pida al usuario si quiere calcular si un número/
#  es primo con for o con while, por tanto, habrá dos funciones que se caracterizan/
#  por hacer ese mismo cálculo de una manera (con for y sin breaks), o de otra (con while)./
#  Ambas funciones devolverá true (si es primo) o false (si no es primo)./
#  El programa principal informará del resultado. /
# Además, como mejora puedes calcular el tiempo que tarda en encontrar la solución de una manera u otra./
#  Comentario: aprovecha el código que tienes ya creado
import os
os.system ('cls')
import time
def fwhile(a):
    inicio = time.time()
    if a <= 0:
        print("Error. Dame un numero mayor que 0: ")
    else:
        divisor = 0
        i = 2
        while (i < a):
            if a % i==0:
                divisor += 1
            i += 1
        if divisor == 0 and a > 1:
            print ("El numero es primo")
        else:
            print ("No es un numero primo")
    final=(time.time()-inicio)
    return "El while tarda: %.10f segundos." %final

def ffor(a):
    inicio=time.time()
    esPrimo=True
    for i in range(a):
        if ((i!=0)and(i!=1) and (a%i==0)):
            esPrimo=False
    if (esPrimo):
            print("El numero es Primo")
    else:
            print("El numero es primo")
    final=time.time()-inicio
    return "El for tarda: %.10f segundos." %final

num=int(input("Dame un numero mayor que 0: "))
funcion=(input("Quieres calcular el numero con ffor o fwhile: "))
if funcion=='ffor':
    print(ffor(num))
else:
    print(fwhile(num))