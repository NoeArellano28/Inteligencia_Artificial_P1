
import os

from collections import deque

cola = deque()

print (cola) 
deque ([])

visitados = []

grafo = {'a': [('d',1), ('f',2), ('g',3)],

'd': [('a',1), ('h',4), ('c',5)], 
'f': [('a', 2), ('b', 6), ('i',7)],
'g': [('a',3)],

'h':[('d', 4), ('k',8)],

'c': [('d',5), ('j', 9)], 
'b': [('f', 6), ('1',8)],

'i': [('f',7), ('m', 7), ('n', 6)],

'k':[('h',8)],

'j':[('c',9), ('x',10)], 
'1':[('b',8), ('z',11)],

'm':[('i',7)],
'n':[('i',6)],

'x':[('j',10)],
'z':[('1',11)],

}

print ("Muestra el grafo antes del recorrido: \n") 
for key, lista in grafo.items():
    print (key)
    print (lista)
    
origen =  input ("Ingresa un nodo de origen: ") 

print ("\nLista de recorrido en lo ancho del arbol\n")

#Paso 1 
cola.append(origen)

#Paso 2

while cola:

#paso 3

    actual = cola.popleft()

#paso 4

    if actual not in visitados:

#paso 5

        print("Vertice actual ->", actual)

#paso 6 
        visitados.append(actual)

#paso 7

    for key, lista in grafo[actual]:

            if key not in visitados:
                        cola.append(key)
