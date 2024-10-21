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

    def __str__(self):
        return str(self.id)

    def getArista(self):
        """
        Método para imprimir los valores de la Arista
        """     
        print(self.nodo0, self.nodo1, self.id)
