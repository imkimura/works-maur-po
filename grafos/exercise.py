class Edge:
    def __init__(self, edgeName, vertexDestiny):        
        self.edgeName = edgeName
        self.vertexDestiny = vertexDestiny

    def getEdge(self):
        return self.edgeName

    def __str__(self):
        return '{} - Aresta' .format(self.edgeName)

class Vertex:
    def __init__(self, vertexName):
        self.vertexName = vertexName
        self.edges = []
        self.edgesIN = []
    
    def __str__(self):
        return '{} - Vértice' .format(self.vertexName)
    
    def setNewEdgeInVertex(self, edgeName, destiny):
        edge = Edge(edgeName, destiny)
        self.edges.append(edge)    

def verifyPath(orign, destiny, edgesPassed):
    
    if len(orign.edges) == 0:
        print('deu ruim')
        return False

    for edge in orign.edges:
        if len(edgesPassed) > 0:
            if edge not in edgesPassed:
                edgesPassed.append(edge)
            else:
                print('ja passei aq')
                return False
        else:
            edgesPassed.append(edge)

        if edge.vertexDestiny == destiny:
            print('{} <---> {}' .format(orign.vertexName, edge.vertexDestiny))   
            print('deu bom aqui')
            return True
        else:         
            print('{} <---> {}' .format(orign.vertexName, edge.vertexDestiny))   
            if verifyPath(edge.vertexDestiny, destiny, edgesPassed):
                print('ok')
                return True
    return False

def verifyCicle(orign, destiny):
    
    if len(orign.edges) == 0:
        print('deu ruim')
        return False

    edgesPassed = []
    if verifyPath(orign, destiny, edgesPassed):
        print('é path')
        edgesPassed = []
        if verifyPath(destiny, orign, edgesPassed):            
            print('e tambem é cicle')
            return True            
    print('mas nao é cicle')
    return False

def isEulerian(graph): 

    for i in range(len(graph)): 
        print(len(graph[i].edges))
        if len(graph[i].edges) % 2 !=0: #verifica se algum vertice tem grau impar mas precisar ver quantas arestas tem em um vertice
            return False
    return True


if __name__ == "__main__":
    v = []
    edgesPassed = []

    v.append(Vertex('A'))
    v.append(Vertex('B'))
    v.append(Vertex('C'))
    v.append(Vertex('D'))
    v.append(Vertex('E'))

    v[0].setNewEdgeInVertex('1', v[3])
    v[1].setNewEdgeInVertex('3', v[0])
    v[2].setNewEdgeInVertex('4', v[1])
    v[0].setNewEdgeInVertex('2', v[2])
    v[3].setNewEdgeInVertex('2', v[4])
    v[4].setNewEdgeInVertex('2', v[0])

    # v[4].setNewEdgeInVertex('5', v[2]) # E - D
    # v[2].setNewEdgeInVertex('6', v[4]) # D - E

    # if verifyPath(v[0], v[4], edgesPassed): # A - E
    #     for p in edgesPassed:
    #         print(p) 
    # else:
    #     print('--------')
    #     for p in edgesPassed:
    #         print(p)
    
    # if verifyCicle(v[0], v[4]): # A - E
    #     for p in edgesPassed:
    #         print(p) 

    if isEulerian(v):
        print('eh euleriano')
    else:
        print('nao eh euleriano')

# TODO
# a) uma função que dados 2 vértices como parâmetros, verifique se há caminho entre eles;

# b) outra função que dado um vértice (origem e tb destino), verifique se há um ciclo no grafo. Considere que para existir um 
#    ciclo deve sair de um vértice, visitar pelo menos outro vértice e, retornar ao vértice de origem.

# c) criar funçao pra verificar se é grafo euleriano

# https://www.geeksforgeeks.org/euler-circuit-directed-graph/?ref=lbp 
