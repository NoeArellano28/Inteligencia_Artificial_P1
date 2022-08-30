
from audioop import reverse         #importamos las funciones especificas de librerias
from pickle import TRUE


lista = ["cero","uno","dos","tres","cuatro", "cinco"] #crear lista
print ("Lista original es " , lista)

print ("Posicion 1: " + lista[1])                     #mostrar lo que esta en la posicion 1

print ("Ultima posicion: " + lista [-1])              #mostrar con numeros negativos la ultima posicion

del lista [3]                                         #eliminar lo que está en la posicion 3 con "del lista []"
print("Eliminando lo que esta en posicion 3: " , lista)

lista.remove("dos")                                   #eliminar elemento ingresando literal con "lista.remove()"
print ('Eliminando el elemento "dos": ', lista)

Guardado = lista.pop(1)         #usando funcion "lista.pop()" para eliminar y guardar un elemento segun su direccion
print (lista)
print ("El elemento que se borro y guardo (posicion 1) es " + Guardado)

lista.append("final")          #agregando un nuevo elemento al final de la lista con la funcion "lista.append ()"
print("Agregando un nuevo elemento al ultimo: " , lista)

lista.insert (0, "inicio") #agregando un elemento a la posicion que quieras con la funcion "lista.insert (posicion, elemento)"
print("Agregando un nuevo elemento al principio: " , lista)

lista.sort()
print("Ordenando la lista en orden alfabetico: " , lista)   #.sort() para orden alfabético 
                                                                #.sorted() para orden alfabetico TEMPORAL
lista.sort(reverse = True)
print("Ordenando la lista en orden inverso: " , lista)      #.sort(reverse = True) para orden inverso

print("El numero de elementos de esta lista es: ", len(lista)) #contando elementos de la lista con "len(lista)"

