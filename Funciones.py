from tkinter import Y

print ("\t\t\tOPERACIONES CON 10 Y 10\n\n".title())
                                        #CON PARAMETROS Y SIN RETORNO
def suma (x,y):                                 #creamos la funcion pidiendo dos valores  
    print ("La suma es: ",x+y)                  #imprimimos la suma de los dos valores
suma(10,10)                                     #mandamos llamar la funcion dandole los dos valores

                                        #CON PARAMETROS Y CON RETORNO
def resta (x,y):                                #creamos la funcion pidiendo dos valores
    return x-y                                  #retornamos lo que salga de la operacion con estos dos valores                             
print ("La resta es: ",resta(10,10))            #imprimimos lo que retorno dandole al mismo tiempo los valores

                                        #SIN PARAMETROS Y SIN RETORNO
def mult ():                                    #creamos la funcion sin pedir nada
    x=10                                        #creamos dos variables
    y=10
    print ("La multiplicacion es: ", x*y)       #imprimimos la respuesta a la operacion
mult()                                          #mandamos llamar a la funcion

                                         #SIN PARAMETROS Y CON RETORNO
def div ():                                     #creamos la funcion sin pedir nada
    x=10                                        #creamos dos variables
    y=10
    return x/y                                  #retornamos la operacion que queremos hacer
print ("La division es:  ", div ())             #imprimimos lo que ahora vale la funcion

