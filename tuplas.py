tupla = ("El resultado de la multiplicacion es: ", 10, 2) #creamos la tupla con 3 elementos
print (tupla[0] , tupla[1] * tupla[2])                    #imprimimos el primer elemento y multiplicamos los otros dos

#LISTA A TUPLA
lista = ["zero", "one", "two", "three", "four"]         #creo una lista
tupla2 = tuple (lista)          #convertimos la lista en una tupla usando "tuple (lista)"
print (tupla2)                  #se ha creado una tupla a partir de lo que tiene la lista e imprimimos 

#AHORA TUPLA A LISTA
tupla3 = ("Inteligencia", "artificial") #creo una tupla
lista3 =list(tupla3)                    #convertimos la tupla en una lista usando "list (tupla)"
print (lista3)                          #se ha creado una lista a partir de lo que tiene la tupla e imprimimos

