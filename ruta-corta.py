import heapq

class Estacion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vecinos = {}  # Diccionario de estaciones vecinas y tiempo de viaje

    def agregar_vecino(self, estacion, tiempo):
        self.vecinos[estacion] = tiempo

def encontrar_ruta(estacion_inicial, estacion_objetivo):
    nodo_inicial = Nodo(estacion_inicial)
    nodo_objetivo = Nodo(estacion_objetivo)
    
    nodos_explorados = []
    heapq.heappush(nodos_explorados, nodo_inicial)
    nodos_visitados = set()

    while nodos_explorados:
        nodo_actual = heapq.heappop(nodos_explorados)

        if nodo_actual.estado == estacion_objetivo:
            # Reconstruir la ruta
            ruta = []
            tiempo_total = 0
            while nodo_actual:
                ruta.append(nodo_actual.estado.nombre)
                if nodo_actual.padre:
                    tiempo_total += nodo_actual.estado.vecinos[nodo_actual.padre.estado]
                nodo_actual = nodo_actual.padre
            return ruta[::-1], tiempo_total

        if nodo_actual.estado in nodos_visitados:
            continue

        nodos_visitados.add(nodo_actual.estado)

        for estacion_vecina, tiempo in nodo_actual.estado.vecinos.items():
            if estacion_vecina not in nodos_visitados:
                nuevo_costo = nodo_actual.costo + tiempo
                nuevo_nodo = Nodo(estacion_vecina, nodo_actual, nuevo_costo)
                heapq.heappush(nodos_explorados, nuevo_nodo)

    return None, None

class Nodo:
    def __init__(self, estado, padre=None, costo=0):
        self.estado = estado
        self.padre = padre
        self.costo = costo

    def __lt__(self, otro):
        return (self.costo) < (otro.costo)

# Crear estaciones
estaciones = {
    1: Estacion(1),
    2: Estacion(2),
    3: Estacion(3),
    4: Estacion(4),
    5: Estacion(5),
    6: Estacion(6)
}