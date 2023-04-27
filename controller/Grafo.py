import networkx as nx
import matplotlib.pyplot as plt

def generarGrafo(listaVertices,listaAristas,habilitarBoton):
    try:
        G = nx.Graph()

        vertices=listaVertices.split(",")

        for element in vertices:
            G.add_node(element)
            
        aristas=listaAristas.split(",")

        for elemento in aristas:
            G.add_edge(elemento[0],elemento[1])
            
        nx.draw(G, with_labels=True)
        habilitarBoton["state"]="normal"
        plt.figure(1)
        plt.show()
        return G
        
    except:
        return False


    #Realizamos el algoritmo de busqueda de anchura
def generarAlgoritmo(G):
    inicio= list(G.nodes)[0]

    ruta=nx.bfs_tree(G,inicio)

    nx.draw(ruta, with_labels=True)
    plt.figure(1)
    plt.show()


