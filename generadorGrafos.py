from generadorNodos import Nodo
from generadorAristas import Arista

class Grafo:
    """
    Clase generadora de Grafos
    """
    def __init__(self, dirigido = False):
        """
        Constructor                                                   
        """
        self.nodos = {}         #Conjunto, para evitar duplicados
        self.aristas = {}
        self.dirigido = dirigido    #Grafo no dirigido como valor de inicio
        self.attr = {
            """
            Diccionario en construcción
            """
        }

    def agregarNodo(self, id):
        """
        Agrega un nuevo nodo al grafo
        """
        nodo = self.nodos.get(id)   #Verifica si el nodo existe
        #Si no existe se crea uno nuevo        
        if nodo == None:
            self.nodos[id] = Nodo(id)
        return self.nodos[id]

    def agregarArista(self, n1, n2, id):
        """
        Agrega una arista al grafo
        """
        arista = self.aristas.get(id)   #Verifica si la arista existe
        #Si no existe se crea uno nuevo        
        if arista == None:
            V0 = self.agregarNodo(n1)   #Agrega nodo base
            V1 = self.agregarNodo(n2)   #Agrega nodo adyacente            
            self.aristas[id] = Arista(V0, V1, id)   #Agrega arista
        return self.aristas[id]

    def __str__(self):
        """
        Convertir grafo en string
        """
        graf = "Nodos: "
        for i in self.nodos:
            graf += str(i) + ','

        graf = "\nAristas: "
        for i in self.aristas:
            graf += str(i) + ','
        return str(graf)
    
    def graphViz(self, id):
        """
        Genera un archivo con formato GraphViz
        """
        cadena = ''
        #Formato DOT
        cadena += 'digraph ' + id + '{\n'
        #Imprimir los nodos
        for nodo in self.nodos:
            cadena += str(nodo) + ';\n'
        #Imprimir las aristas
        for key, arista in self.aristas.items():
            cadena += str(arista) + ';\n'
        #Final del formato
        cadena += '}'

        nombreArchivo = id + '.gv'
        #Escribimos el archivo de salida
        archivo = open(nombreArchivo, 'w+')
        archivo.write(cadena)
        archivo.close()
        print('Archivo GraphViz generado:' + nombreArchivo + '\n')
        