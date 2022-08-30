
 
x=0                                                 #creamos la variable x con valor 0

while x<10:                                         #mientras x sea menor que 10 ejecuta:
    
    x+=1                                            #suma un valor a x
    if x==5 or x==7:                                #si x vale 5 o 7 ejecuta:
        continue                                    #salta todo lo que este despues de aqui y haz de nuevo el while
    print (x)                                       #imprime la variable 
    print ("Estoy dentro del while")                #imprime un mensaje
    print ("esta instruccion se realizara porque NO TENGO el CONTINUE\n")    #imprime un mensaje




