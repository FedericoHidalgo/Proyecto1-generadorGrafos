class Arista:
    """
    Clase generadora de Aristas
    """
    def __init__(self,nodo0, nodo1, id, dirigido = False):
        """
        Constructor
        """
        self.nodo0 = nodo0  #Nodo de origen
        self.nodo1 = nodo1  #Nodo de destino  
        self.id =  id       #Identificador de la arista
        self.dirigido = dirigido #Arista definida o no
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

    def getArista(self):
        """
        Método para imprimir los valores de la Arista
        """     
        print(self.nodo0, self.nodo1, self.id)
