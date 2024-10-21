class Nodo:
    def __init__(self, valor):
        """
        Constructor de la clase Nodo
        """
        self.valor = valor
        self.attr = {
            """
            Diccionario en construcción
            """
        }

    def getNodo(self):
        print("El nodo es:")
        print(self.valor)

nodo1 = Nodo(5)
nodo2 = Nodo(12)

nodo1.getNodo()
nodo2.getNodo()