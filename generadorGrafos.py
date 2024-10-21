class Nodo:
    """
    Clase generadora de Nodos
    """
    def __init__(self, id):
        """
        Constructor
        """
        self.id = id      #Identificador del nodo
        self.attr = {
            """
            Diccionario en construcción
            """
        }

    def __str__(self):
        """
        Convertir nodo en string
        """
        return str(self.id)

    def getNodo(self):
        """
        Método para imprimir el identificador del nodo
        """
        print(self.id)

class Arista:
    """
    Clase generadora de Aristas
    """
    def __init__(self,nodo0, nodo1, id):
        """
        Constructor
        """
        self.nodo0 = nodo0  #Nodo de origen
        self.nodo1 = nodo1  #Nodo de destino  
        self.id =  id       #Identificador de la arista
        self.attr = {
            """
            Diccionario en construcción
            """
        }

    def getArista(self):
        """
        Método para imprimir los valores de la Arista
        """     
        print(self.nodo0, self.nodo1, self.id)

n1 = Nodo(1)
n2 = Nodo(2)

print(n1)
print(n2)