conjunto3 = set()

conjunto1 = {"nissan", "toyota","mistubishi","subaru","susuki","honda",}

conjunto2 = {"Chverolet","Ford","Dodge","Chrysler"}

print ("\n\tEl conjunto 1 contiene: ",len(conjunto1), " elementos que son: \n\t\t", conjunto1)
print ("\n\tEl conjunto 2 contiene: ",len(conjunto2), " elementos que son: \n\t\t", conjunto2)

conjunto2.update([10,20,30,40])
conjunto1.update([10,11,20,22,30])
print ("\nColocando mas elementos a ambos conjuntos de distinto tipo:  ")

print ("\n\tEl conjunto 1 ahora contiene: ",len(conjunto1), " elementos que son: \n\t\t", conjunto1)
print ("\n\tEl conjunto 2  ahora contiene: ",len(conjunto2), " elementos que son: \n\t\t", conjunto2)

conjunto1.discard("susuki")
print ("\n Eliminando SUSUKI del primer conjunto quedaria: \n\t\t", conjunto1)

conjunto3= conjunto1 & conjunto2
print ("\n\tSi colocamos los elementos en comun a un tecer conjunto nos quedaria:\n\t\t\t ", conjunto3)



