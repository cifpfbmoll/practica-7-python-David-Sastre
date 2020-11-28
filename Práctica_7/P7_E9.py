#Escribe un programa que pida dos palabras las pase como parámetro a un procedimiento/
# y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman./
# Si coinciden solo las dos últimas tiene que decir que riman un poco y si no, que no riman.
palabra1=input("Dime una palabra: ")
palabra2=input("Dime otra palabra: ")
def f(a,b):
    if a[-1]==b[-1]:
        if a[-2]==b[-2]:
            if a[-3]==b[-3]:
                print ("Riman, ¡Eres un poeta!")
            else:
                print("Las palabra riman un poco")
        else:
            print("Las palabras no riman")
    else:
        print("Las palabras no riman")
f(palabra1,palabra2)

