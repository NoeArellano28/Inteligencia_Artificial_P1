import cv2
import os
import numpy as np
import random
# Definir el mapa de la ciudad y las ciudades que queremos visitar
ciudades_mapa = {
    'Cancún': {'Mérida': 320, 'Cozumel': 75, 'Playa del Carmen': 68},
    'Mérida': {'Cancún': 320, 'Cozumel': 225, 'Playa del Carmen': 202},
    'Cozumel': {'Cancún': 75, 'Mérida': 225, 'Playa del Carmen': 20},
    'Playa del Carmen': {'Cancún': 68, 'Mérida': 202, 'Cozumel': 20}
}

# Obtener la ciudad de partida que ingresa el usuario
ciudad_partida = input("Ingresa la ciudad de partida: ")

# Verificar si la ciudad de partida ingresada por el usuario es válida
if ciudad_partida not in ciudades_mapa:
    print(f"La ciudad {ciudad_partida} no está en el mapa")
else:
    # Definir las ciudades a visitar y eliminar la ciudad de partida de la lista
    ciudades = list(ciudades_mapa.keys())
    ciudades.remove(ciudad_partida)

    # Definir la función de costo para el algoritmo Hill Climbing
    def costo(ruta):
        distancia_total = ciudades_mapa[ciudad_partida][ruta[0]] # Distancia desde la ciudad de partida a la primera ciudad de la ruta
        for i in range(len(ruta) - 1):
            distancia_total += ciudades_mapa[ruta[i]][ruta[i + 1]]
        return distancia_total

    # Definir la función Hill Climbing
    def hill_climbing():
        # Inicializar la ruta con la mejor opción de recorrido
        mejor_ruta = sorted(ciudades, key=lambda ciudad: ciudades_mapa[ciudad_partida][ciudad])
        mejor_costo = costo(mejor_ruta)

        # Iterar hasta que no se pueda mejorar más la ruta
        while True:
            # Encontrar todas las rutas vecinas
            vecinos = []
            for i in range(len(ciudades)):
                for j in range(i + 1, len(ciudades)):
                    vecino = mejor_ruta.copy()
                    vecino[i], vecino[j] = vecino[j], vecino[i]
                    vecinos.append(vecino)

            # Evaluar el costo de cada ruta vecina y seleccionar la mejor
            mejor_vecino = vecinos[0]
            mejor_costo_vecino = costo(mejor_vecino)
            for vecino in vecinos:
                vecino_costo = costo(vecino)
                if vecino_costo < mejor_costo_vecino:
                    mejor_vecino = vecino
                    mejor_costo_vecino = vecino_costo

            # Si no se puede mejorar más la ruta, regresar la mejor solución encontrada
            if mejor_costo_vecino >= mejor_costo:
                return mejor_ruta

            # De lo contrario, actualizar la ruta actual y continuar buscando
            mejor_ruta = mejor_vecino
            mejor_costo = mejor_costo_vecino

    ruta_optima = hill_climbing()
    print(f"La mejor ruta para visitar las ciudades empezando por {ciudad_partida}")
    print(ruta_optima)
