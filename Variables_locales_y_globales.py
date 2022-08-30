

vglobal =int( input("Ingresa una variable (sera global): \n\t"))      #le pedimos que ingrese el valor de una variable que pusimos gloabl

def funcion ():                                                       #creamos una funcion
    vlocal = int(input("Ingresa otra variable (sera local): \n\t"))   #dentro de la funcion le pedimos que ingrese otro valor para ponerlo en una variable local  
    return vglobal+vlocal                                             #retornamos el valor de la suma de ambas variables  
print("La suma de ambas variables es: ", funcion())                   #imprimimos lo que retorno la funcion

