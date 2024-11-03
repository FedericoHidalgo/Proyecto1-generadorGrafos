import random, math
from generadorGrafos import Grafo

def modeloErdosRenyi(n, m, dirigido = False):
    """
    Crea n vertices y elige al azar m pares de
    vertices para formar las aristas
    """
    G = Grafo(dirigido)
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

def modeloGilbert(p, n, dirigido = False):
    """
    Crea m aristas y n vértices, coloca una
    arista entra cada par independiente y de
    forma uniforme con probabilidad p
    """
    G = Grafo(dirigido)
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

def modeloGeograficoSimple(n, r, dirigido = False):
    """
    Coloca n vértices en un rectangulo unitario
    con coordenadas normales y coloca una arista
    entre cada par que queda a distancia r o menor
    """
    G = Grafo(dirigido)
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

def listaAleatoria(inicio, fin):
    """
    Método que genera una lista de números aleatorios
    """
    lista = random.sample(range(inicio, fin), fin-inicio)
    return lista

def modeloBarabasiAlbert(n, d=0, dirigido = False):
    """
    Colocar n nodos uno por uno, asignando a cada uno d aristas 
    a vértices distintos de tal manera que la probabilidad de que 
    el vértice nuevo se conecte a un vértice existente v es 
    proporcional a la cantidad de aristas que v tiene actualmente.
    """
    G = Grafo(dirigido)  
    #Diccionario de grados de conexión para cada nodo
    grado = {}  
    #Creamos los nodos
    for i in range(n):
        G.agregarNodo(i)
        #A cada nodo le corresponde un grado cero al ser creado
        grado[i] = 0 
    for i in range(1, n):
        #print("\nNodo origen: ", i)
        lista = listaAleatoria(0, i)
        #print("Lista aleatoria creada: ", lista)
        for j in range(i):
            #print("Posición a evaluar: ", j)
            gradoRandom = grado.get(lista[j])
            #print("Nodo destino: ", lista[j])
            #print("Grado del nodo: ", gradoRandom)
            p = 1 - (gradoRandom / d)
            #print("Probabilidad de conexión: ", p)
            r = random.random()
            #print("Num random: ", r)
            #print("1) r < p: ", r, " < ", p)
            if r < p:
                #print("OK")
                #print("2) ¿Es el mismo nodo?")
                if lista[j] != i:
                    #print("No, se realiza la conexión")
                    G.agregarArista(i, lista[j], ' -> ')
                    #print("Grado de origen", i, ":", grado.get(i))
                    #print("Grado de destino", lista[j], ":", grado.get(lista[j]))
                    grado[lista[j]] += 1 
                    grado[i] += 1
                    #print("Nuevo grado de origen", i, ":", grado.get(i))
                    #print("Nuevo grado de destino", lista[j], ":", grado.get(lista[j])) 
                else:
                    pass
                    #print("Si, no se conecta")
            else:
                pass
                #print("No se cumple la condición 1")
    #G.getDiccionarios()
    print("Grado del grafo creado: ", grado)
    return G

#Numero de muestras que se graficaran por modelo
#numNodos = [30, 100, 500]
numNodos = [100]
d = 8
#Modelo Barabasi Albert
for i in numNodos:
    #Generamos el modelo para 30, 100 y 500 nodos
    modelo = modeloBarabasiAlbert(i, d)
    nombreArchivo = "Barabasi-Albert " + str(i) + " nodos"
    #Generamos el archivo .gv
    modelo.graphViz(nombreArchivo)