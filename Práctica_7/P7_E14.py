#Aprovechando el potencial de los diccionarios, escribe un programa que llame a un procedimiento,/
# que recibe como parámetro la fecha en números y devuelve la fecha  con el nombre del mes./
# Comentario: no es necesario validar si la es correcta, damos por hecho que lo será.
def f(a):
    dia=a[0:2]
    mes=a[3:5]
    año=a[6:10]
    meses={"01": "Enero","02": "Febrero","03": "Marzo","04": "Abril","05": "Mayo","06": "Junio","07": "Julio", "08": "Agosto",
            "09": "Septiembre","10": "Octubre", "11": "Noviembre", "12": "Diciembre"}
    for k, v in meses.items():
        if mes==k:
            meses1=meses.get(k)
    print (dia," de ",meses1," de ",año)
fecha=input("Escribe una fecha con el formato dd/mm/aaaa: ")
(f(fecha))


