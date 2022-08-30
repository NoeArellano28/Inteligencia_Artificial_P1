#!/usr/bin/env phyton
# _*_ coding: cp1252 _*_
# _*_ coding: 850 _*_       #libreria para uso de acentos
# _*_ coding: utf-8 _*_


autos = {                               #creamos el diccionario principal

"diccionario1" : {                      #creamos el diccionario 1 dentro del prncipal
    "Marca ": "Nissan",
    "Modelo ": "GTR",
    "Año ": "2000",
    },

"diccionario2" : {                      #creamos el diccionario 1 dentro del prncipal
    "Marca ": "Honda",
    "Modelo": "Accord",
    "Año": "2005",
    }
}

print ("  Mi diccionario principal cuenta con " , len(autos),  " diccionarios\n\n ")        #imprimimos el numero de diccionarios que tiene el principal

print (" El diccionario 1 contiene: \n\t")      #mostramos las categorias con sus elementos del primer diccionario
for x,y in autos["diccionario1"].items():
    print (x,": ",y)

print ("\n\n El diccionario 2 contiene: \n\t")  # #mostramos las categorias con sus elementos del segundo diccionario
for x,y in autos["diccionario2"].items():
    print (x,": ",y)


opc = str (input("\n\t\tDesea eliminar algun diccionario (si o no)?"))  #le pedimos que ingrese si quiere eliminar o no un diccionario

if opc == "si":     #si dice que si, entonces...

        opc2 = int (input("\n\t\tEliminar dicc1 presione 1\n\t\t Eliminar dicc2 presione 2\n"))     #le pedimos que ingrese cual diccionario desea eliminar

        if opc2 == 1:                               #si desea eliminar el primero entonces...
           del autos["diccionario1"]                #eliminamos el dicc1 con 'del'
        if opc2==2:                                 #si desea eliminar el segundo entonces...
            del autos["diccionario2"]               #eliminamos el dicc2 con 'del'

        print ("Quedaria: \n\n\t\t")                #mostramos el resultado final
        print (autos)

else:        #si dice que no, entonces...
        print ("BYE")
    
