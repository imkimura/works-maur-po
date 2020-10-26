from edge import Edge
from vertex import Vertex


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

    v.append(Vertex('A')) #0
    v.append(Vertex('B')) #1
    v.append(Vertex('C')) #2
    v.append(Vertex('D')) #3
    v.append(Vertex('E')) #4
    v.append(Vertex('F')) #5
    v.append(Vertex('G')) #6
    v.append(Vertex('H')) #7
    v.append(Vertex('L')) #8
    v.append(Vertex('J')) #9
    v.append(Vertex('K')) #10
    v.append(Vertex('M')) #11

    v[0].setNewEdgeInVertex('1', v[1])
    v[1].setNewEdgeInVertex('1', v[2])
    v[2].setNewEdgeInVertex('1', v[3])
    v[2].setNewEdgeInVertex('1', v[3])
    v[2].setNewEdgeInVertex('1', v[3])

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

# c) criar funçao pra verificar se é grafo euleriano e criar array com grafo

# d) hamilton

# https://www.geeksforgeeks.org/euler-circuit-directed-graph/?ref=lbp 
