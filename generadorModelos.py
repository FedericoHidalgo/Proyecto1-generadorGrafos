import random, math
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

def modeloGilbert(p, n):
    """
    Crea m aristas y n vértices, coloca una
    arista entra cada par independiente y de
    forma uniforme con probabilidad p
    """
    G = Grafo()
    #Creamos los nodos
    for i in range(n):
        G.agregarNodo(i)
    #Creamos las aristas
    for i in range(n):
        for j in range(n):
            #La arista se crea si es menor a p
            if random.random() < p:
                #No se crea aristas hacia el mismo nodo
                if(j != i):
                    G.agregarArista(i, j,' -> ')
    return G

def distanciaNodos(n1, n2):
    """
    Método que calcula la distancia entre dos puntos
    representados por nodos
    """
    #Coordenadas 'X' n_[0]
    #Coordenadas 'Y' n_[1]
    n1 = list(n1)
    n2 = list(n2)
    d = math.sqrt((n2[0] - n1[0])**2 + (n2[1] - n1[1])**2)
    return d

def modeloGeograficoSimple(n, r):
    """
    Coloca n vértices en un rectangulo unitario
    con coordenadas normales y coloca una arista
    entre cada par que queda a distancia r o menor
    """
    G = Grafo()
    #Diccionario de coordenadas para cada nodo
    posicion = {}
    #Creamos los nodos
    for i in range(n):
        G.agregarNodo(i)
        #A cada nodo i le corresponde una coordenada {x,y} 
        #de valor (0,0) hasta (1,1) generada con random
        x = random.random()
        y = random.random()
        posicion[i] = {x, y}        
    print("Diccionario de posición: ")
    print(posicion.items())
    #Se crea una arista entre cada par de nodos con distancia
    #menor a r
    for i in range(n):
        n1 = posicion.get(i)    #Coordenadas del nodo "i"        
        for j in range(n):
            n2 = posicion.get(j)    #Coordenadas del nodo "j"
            #No se crea aristas hacia el mismo nodo
            if i != j:
                #Obtenemos distancia r
                d = distanciaNodos(n1, n2)
                if d <= r:
                     G.agregarArista(i, j,' -> ')
    return G

def modeloBarabasiAlbert():
    """
    Colocar n nodos uno por uno, asignando a cada uno d aristas 
    a vértices distintos de tal manera que la probabilidad de que 
    el vértice nuevo se conecte a un vértice existente v es 
    proporcional a la cantidad de aristas que v tiene actualmente.
    """