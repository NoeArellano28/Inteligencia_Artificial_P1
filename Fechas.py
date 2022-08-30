import datetime                             #importamos la libreria necesaria para mostrar fechas

x = datetime.datetime.now()                 #asignamos a una variable el metodo que nos dira la fache en eset caso de hoy porque puse "now()"

print("La fecha de hoy es: \t\t\t")         #imprimimos un mensaje
print (x.strftime("%x"))                    #con la funcion .srtftime() pones dentro de los parentesis lo que quieras mostrar especificamente

print("\n\nLa hora de hoy es: \t\t\t")
print (x.strftime("%X"))