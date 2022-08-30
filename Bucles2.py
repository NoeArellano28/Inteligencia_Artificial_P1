
tupla = ("Pans Rojo ","Pans Verde ","Pans Azul ")           #creamos la primera tupla
tupla2 = ("Camisa roja","Camisa Verde","Camisa Azul")       #creamos la segunda tupla

print ("\t\tCOMBINACION DE OUTFITS\n\n")                    #imprimimos un titulo
c = 0                                                       #inicializamos el valor de nuestro acumulador en 0
for x in tupla:                                             #creamos el primer for para que pase por la primera tupla
     for y in tupla2:                                       #creamos el segundo for para que pase por la segunda tupla
         c+=1                                               #le agregamos uno al contador
         print (c, " Combinacion es:   -->",x+y)            #imprimimos la suma de las dos tuplas junto con el del contador

