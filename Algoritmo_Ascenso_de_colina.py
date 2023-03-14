import random

# Definir el mapa de la ciudad y las ciudades que queremos visitar
ciudades_mapa = {
    'Cancún': {'Mérida': 320, 'Cozumel': 75, 'Playa del Carmen': 68},
    'Mérida': {'Cancún': 320, 'Cozumel': 225, 'Playa del Carmen': 202},
    'Cozumel': {'Cancún': 75, 'Mérida': 225, 'Playa del Carmen': 20},
    'Playa del Carmen': {'Cancún': 68, 'Mérida': 202, 'Cozumel': 20}
}
ciudades = ['Cancún', 'Mérida', 'Cozumel', 'Playa del Carmen']

# Definir la función de costo para el algoritmo Hill Climbing
def costo(ruta):
    distancia_total = 0
    for i in range(len(ruta) - 1):
        distancia_total += ciudades_mapa[ruta[i]][ruta[i + 1]]
    return distancia_total

# Definir la función Hill Climbing
def hill_climbing():
    # Inicializar la ruta aleatoria
    ruta_actual = random.sample(ciudades, len(ciudades))
    costo_actual = costo(ruta_actual)
    
    # Iterar hasta que no se pueda mejorar más la ruta
    while True:
        # Encontrar todas las rutas vecinas
        vecinos = []
        for i in range(len(ciudades)):
            for j in range(i + 1, len(ciudades)):
                vecino = ruta_actual.copy()
                vecino[i], vecino[j] = vecino[j], vecino[i]
                vecinos.append(vecino)
        
        # Evaluar el costo de cada ruta vecina y seleccionar la mejor
        mejor_vecino = vecinos[0]
        mejor_costo = costo(mejor_vecino)
        for vecino in vecinos:
            vecino_costo = costo(vecino)
            if vecino_costo < mejor_costo:
                mejor_vecino = vecino
                mejor_costo = vecino_costo
        
        # Si no se puede mejorar más la ruta, regresar la mejor solución encontrada
        if mejor_costo >= costo_actual:
            return ruta_actual
        
        # De lo contrario, actualizar la ruta actual y continuar buscando
        ruta_actual = mejor_vecino
        costo_actual = mejor_costo
        
ruta_optima = hill_climbing()
print(ruta_optima)
