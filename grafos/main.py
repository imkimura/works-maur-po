from edge import Edge
from vertex import Vertex
import graph as gp


if __name__ == "__main__":
    graph = []
    edgesPassed = []
    fila = []

    graph.append(Vertex('A')) #0
    graph.append(Vertex('B')) #1
    graph.append(Vertex('C')) #2
    graph.append(Vertex('D')) #3

    graph[0].setNewEdgeInVertex('AC', graph[2])
    graph[2].setNewEdgeInVertex('CB', graph[1])
    graph[1].setNewEdgeInVertex('BD', graph[3])
    graph[3].setNewEdgeInVertex('DC', graph[2])
    graph[2].setNewEdgeInVertex('CA', graph[0])
    graph[0].setNewEdgeInVertex('AB', graph[1])
    graph[1].setNewEdgeInVertex('BA', graph[0])

    if gp.verifyPath(graph[0], graph[3], edgesPassed): # A - D   
        print('\n-------- tem caminho ---------\n')
        print('{} <---> {}' .format(graph[0], graph[3]))        
        for edge in edgesPassed:
            print('{}' .format(edge))   
    else:
        print('não tem caminho')
    
    edgesPassed = []
    
    if gp.verifyCicle(graph[0], graph[0]): 
        print('\n-------- é hamiltoniano ---------\n')
        gp.showPathHamilton(graph)

    if gp.isEulerian(graph):
        print('\n-------- é euleriano ---------\n')
        gp.showPathEulerian(graph)
    else:
        print('nao eh euleriano')

    print('\n-------- busca largura ---------\n')
    gp.buscaLargura(fila, graph, edgesPassed)

    edgesPassed = []
    fila = []

    print('\n-------- busca profundidade ---------\n')
    gp.buscaProfundidade(fila, graph, edgesPassed)

# TODO
# a) uma função que dados 2 vértices como parâmetros, verifique se há caminho entre eles;

# b) outra função que dado um vértice (origem e tb destino), verifique se há um ciclo no grafo. Considere que para existir um 
#    ciclo deve sair de um vértice, visitar pelo menos outro vértice e, retornar ao vértice de origem.

# c) criar funçao pra verificar se é grafo euleriano e criar array com grafo

# d) hamilton

# e) busca por largura e busca por profundidade

# https://www.geeksforgeeks.org/euler-circuit-directed-graph/?ref=lbp 
