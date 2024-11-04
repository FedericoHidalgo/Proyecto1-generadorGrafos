from generadorModelos import *
#Numero de muestras que se graficaran por modelo
numNodos = [30, 100, 500]

#Modelo Erdos - Renyi
for i in numNodos:
    #Generamos el modelo para 30, 100 y 500 nodos
    modelo = modeloErdosRenyi(i, i-1)
    nombreArchivo = "Erdos-Renyi " + str(i) + " nodos"
    #Generamos el archivo .gv
    modelo.graphViz(nombreArchivo)

#Modelo Gilbert
p = 0.1
#Damos una probabilidad de 0.1 para la conexión de nodos
for i in numNodos:
    #Generamos el modelo para 30, 100 y 500 nodos
    modelo = modeloGilbert(p, i)
    nombreArchivo = "Gilbert "  + str(i) + " nodos"
    #Generamos el archivo .gv
    modelo.graphViz(nombreArchivo)

#Modelo Geografico Simple
r = 0.1 #Distancia máxima entre nodos
for i in numNodos:
    #Generamos el modelo para 30, 100 y 500 nodos
    modelo = modeloGeograficoSimple(i, r)
    nombreArchivo = "GeograficoSimple " + str(i) + " nodos"
    #Generamos el archivo .gv
    modelo.graphViz(nombreArchivo)

#Modelo Barabasi-Albert
d = 8 #Número máximo de conexiones por vertice
for i in numNodos:
    #Generamos el modelo para 30, 100 y 500 nodos
    modelo = modeloBarabasiAlbert(i, d)
    nombreArchivo = "Barabasi-Albert " + str(i) + " nodos"
    #Generamos el archivo .gv
    modelo.graphViz(nombreArchivo)

for i in numNodos:
    #Generamos el modelo para 30, 100 y 500 nodos
    modelo = modeloDorogovtsevMendes(i)
    nombreArchivo = "Dorogovtsev-Mendes " + str(i) + " nodos"
    #Generamos el archivo .gv
    modelo.graphViz(nombreArchivo)