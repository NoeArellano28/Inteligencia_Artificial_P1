marca = str (input("\tMenciona una marca de autos japoneses \n\t")).title() #imprimimos un mensaje y un input para que el usuario ingrese algo

lista = ["Mazda","Honda","Toyota","Nissan","Mitsubishi","Susuki","Subaru"]  #creamos una lista con ciertos elementos

if marca in lista:                                                          #si la variable que se ingreso esta en la lista entonces:
    print ("\nLa marca "+ marca + " SI es japonesa")                        #se imprime este mensaje
else:                                                                       #de lo contrario
    print("\nla marca "+ marca + " NO es japonesa")                         #se imprime este mensaje


tupla = ("Mazda","Honda","Nissan","Mitsubishi","Susuki","Subaru")           #creamos una tupla con ciertos elementos en ella 
auto = str (input("Que marca es el auto de Brian O'conner en la primera pelicula?")).title()    #imprimimos un mensaje y un input para que el usuario ingrese algo

if auto in tupla:                                                       #si la variable que se ingreso esta en la tupla entonces:
    print ("Estas cerca pero no es "+auto)                              #se imprime este mensaje
elif auto == "Toyota":                                                  #si la variable que se ingreso es igual a cierto elemento entonces:
    print ("CORRECTO! Si es un: "+ auto)                                #se imprime este mensaje
else:                                                                   #si no es cualquiera de lo anterior entonces:
    print ("INCORRECTO! " + auto + " ni si quiera es una marca japonesa")   #se imprime este mensaje