#Desarrolla un programa, que nos sirva para gestionar nuestros contactos/
# (la información a gestionar será el teléfono, nombre, apellido1, apellido2 y correo electrónico./
# El programa tendrá un menú, con las siguientes opciones: añadir contacto,/
# consultar contacto a partir de la clave, consultar todos los contactos y eliminar contacto./
# Aprovecha lo que has aprendido hasta el momento (diccionarios, funciones, procedimientos…).
contacto={"Roberto": ['torres', 'cruz', 111,'email@inventado'],
 "Enrique": ['manuel', 'cocacola', 222, 'email2@inventado']}
agenda=True
def añadir(contacto):
    nombre=str(input("Escribe el nombre del contacto: "))
    apellido1=str(input("Escribe el primer apellido: "))
    apellido2=str(input("Escribe el segundo apellido: "))
    telefono=int(input("Escribe el número de teléfono: "))
    email=str(input("Escribe el correo electrónico: "))
    lista_contacto=[telefono, apellido1, apellido2, email]#Valores del diccionario
    contacto[nombre]=lista_contacto#K principal=nombre
    return contacto

def eliminar(contacto):
    eliminarContacto=str(input("¿Qué contacto quieres eliminar? "))
    print ("¿Estás seguro?")
    check=input("Si/No ")
    if check=="Si" or check=="si" or check=="SI":
        contacto.pop(eliminarContacto)
        print("El contacto se ha eliminado correctamente. Ya no eres su amigo.")
    else:
        print("El contacto no se ha eliminado.")

def consultarTodo(contacto):
    for k, v in contacto.items():
        print (k, v)

def consultaContacto(contacto):
    consulta=input("¿Que contacto quieres consultar?: ")
    error="No se encuentra el contacto"
    print(contacto.get(consulta, error))

while agenda:
    print("=====================")
    print(" AGENDA DAVID SASTRE ")
    print("=====================")
    print("1- Añadir Contacto")
    print("2- Consultar Contacto") 
    print("3- Consultar todos los contactos")
    print("4- Eliminar contacto")
    menu=int(input("Elige una opción del 1 al 4: "))
    if menu==1:
        añadir(contacto)
        print(contacto)
    elif menu==2:
        consultaContacto(contacto)
    elif menu==3:
        consultarTodo(contacto)
    elif menu==4:
        eliminar(contacto)
        print(contacto)
    else:
        Agenda=False
