class Usuario:													#cremos la clase principal
	def __init__ (self, nom, apell):							#definimos la funcion constructora
		self.nombre = nom										#le asignamos el primer valor del parametro a nombre
		self.apellidos = apell									#le asignamos el segundo valor del parametro a apellidos

	def imprime_datos(self):									#creamos otra funcion que solo muestre los datos
		print("Cliente normal (SUPERCLASE):\n\t")				#imprimimos un mensaje
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)		#imprimimos lo que tiene la clase en nombre y apellidos

usuario1 = Usuario("Noe","Arellano\n\n\t")			#creamos el objeto dandole sus parametros constructores 

usuario1.imprime_datos()							#mandamos llamar la funcion que imprime datos 


class VIP(Usuario):											#cremos la subclase que hereda de la principal
	def __init__ (self, nom,apell, numVIP):					#definimos la funcion constructora de esta subclase
		Usuario.__init__ (self,nom,apell)					#heredamos la funcion __init__ de la clase principal
		self.NumeroVIP =numVIP								#le asignamos el nuevo parametro que tendra esta clase a NumeroVIP
	def imprime_datos(self):								#creamos otra funcion que solo muestre los datos
		print("Cliente VIP (SubClase):\n\t")				#imprimimos un mensaje
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos, "\nNumero VIP: ", self.NumeroVIP)		##imprimimos lo que tiene la subclase en nombre y apellidos y en su nuevo parametro VIP

usuario2 = VIP("Jesus ","Carrillo", 1234)		#creamos el objeto dandole sus parametros constructores

usuario2.imprime_datos()						#mandamos llamar la funcion que imprime datos
