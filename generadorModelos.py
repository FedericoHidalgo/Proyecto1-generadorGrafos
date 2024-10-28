import random
from generadorGrafos import Grafo

def modeloErdosRenyi(n, m):
    """
    Crea n vertices y elige al azar m pares de
    vertices para formar las aristas
    """
    G = Grafo()
    #Creamos los nodos
    for i in range(n):
        G.agregarNodo(i)
    #Creamos las aristas
    for i in range(m):
        #Nodo aleatorio 1
        v1 = random.randint(0, n-1)
        #Nodo aleatorio 2
        v2 = random.randint(0, n-1)
        #Si v1 != v2 creamos una arista
        if v1 != v2:
            G.agregarArista(v1, v2,' -> ')
    return G

def modeloGilbert():
    """
    Crea m aristas y n vértices, coloca una
    arista entra cada par independiente y de
    forma uniforme con probabilidad p
    """