
print("\n\t\t CALCULO DE EL AREA DE UN TRIANGULO\n\n\t")            #imprimimos un mensaje

b = int(input("Introduce el valor de la base:  "))                  #pedimos que ingrese el valor b
h = int(input("Introduce el valor de la altura:  "))                #pedimos que ingrese el valor h
def funcion (b,h):                                                  #creamos una funcion con los parametros anteriores
    global r                                                        #hacemos que el resultado sea una variable global
    r= (b*h/2)                                                      #a "r" le asignamos el valor de la operacion realizada con los parametros
    print ("\n El resultado es: ", r)                               #imprimimos el resultado

funcion (b,h)                                       #mandamos llamar la funcion asignandole los valores que pedimos como parametros

#AHORA OTRA FUNCION PERO CON LAMBDA
x = int(input("Sumale un numero al resultado anterior:  ")) #pedimos el valor del parametro

funcion = lambda cte:  r+cte                                #creamos la funcion con lambda con un parametro y realizamo la operacioon
print("\n\t\tEl resultado es: ",funcion(x))                 #imprimimos lo que resulto de la funcion
