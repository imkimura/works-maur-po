class Edge:
    def __init__(self, edgeName, vertexDestiny):        
        self.edgeName = edgeName
        self.vertexDestiny = vertexDestiny

    def getEdge(self):
        return self.edgeName

class Vertex:
    def __init__(self, vertexName):
        self.vertexName = vertexName
        self.edges = []
    
    def setNewEdgeInVertex(self, edgeName, o):
        edge = Edge(edgeName, o)
        self.edges.append(edge)

if __name__ == "__main__":
    v = []

    v.append(Vertex('A'))
    v.append(Vertex('B'))



    v[0].setNewEdgeInVertex('a', v[1])


    # v.setNewAresta('a')

    print(v[0].edges[0].vertexDestiny.vertexName)

# TODO
# a) uma função que dados 2 vértices como parâmetros, verifique se há caminho entre eles;

# b) outra função que dado um vértice (origem e tb destino), verifique se há um ciclo no grafo. Considere que para existir um 
#    ciclo deve sair de um vértice, visitar pelo menos outro vértice e, retornar ao vértice de origem.

# c) criar funçao pra verificar se é grafo euleriano
