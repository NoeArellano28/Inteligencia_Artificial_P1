
import re                           #importamos la libreria re

texto = "La funcion search() busca coincidencias con lo que le pides, pero al encontrar una primera coincidencia ahi se queda" #creamos variable str
buscar = re.search("search()" , texto)  #a la variable "buscar" le asignamos lo que nos haga la funcion
print (buscar)

texto = "La funcion findall() busca todas las codiciones que sean iguales" #creamos variable str
buscar = re.findall("a" , texto)    #a la variable "buscar" le asignamos lo que nos haga la funcion
print (buscar)                      #imprimimos el resultado

texto = "La funcion split() busca lo que le ingrese y me muestra todo menos eso que puse" #creamos variable str
buscar = re.split(" " , texto)  #a la variable "buscar" le asignamos lo que nos haga la funcion
print (buscar)                      #imprimimos el resultado

texto = "La funcion sub() reemplaza las coincidencias por lo que le especifiquemos en el segundo argumento" #creamos variable str
buscar = re.sub("a" , "e" ,texto)   #a la variable "buscar" le asignamos lo que nos haga la funcion
print (buscar)                      #imprimimos el resultado
