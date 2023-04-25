import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

vertices = input("Ingrese los vertices separados por comas:").split(",")

for element in vertices:
    G.add_node(element)
    
aristas=input("Ingrese las aristas separadas por comas: ").split(",")

for elemento in aristas:
    G.add_edge(elemento[0],elemento[1])
    
nx.draw(G, with_labels=True)
plt.show()


#Realizamos el algoritmo de busqueda de anchura

inicio= list(G.nodes)[0]

ruta=nx.bfs_tree(G,inicio)

nx.draw(ruta, with_labels=True)
plt.show()