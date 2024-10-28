from generadorModelos import *
#Numero de muestras que se graficaran por modelo
numNodos = [30, 100, 500]

#Modelo Erdos - Renyi
for i in numNodos:
    modelo = modeloErdosRenyi(i, i-1)
    nombreArchivo = "Erdos-Renyi " + str(i) + " nodos"
    modelo.graphViz(nombreArchivo)