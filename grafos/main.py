from edge import Edge
from vertex import Vertex
import graph as gp


if __name__ == "__main__":
    graph = []
    edgesPassed = []
    fila = []

    graph.append(Vertex('Um')) #0
    graph.append(Vertex('Dois')) #1
    graph.append(Vertex('Tres')) #2
    graph.append(Vertex('Quatro')) #3
    graph.append(Vertex('Cinco')) #4
    graph.append(Vertex('Seis')) #5
    graph.append(Vertex('Sete')) #6
    graph.append(Vertex('Oito')) #7
    graph.append(Vertex('Nove')) #8
    graph.append(Vertex('Dez')) #9
    graph.append(Vertex('Onze')) #10

    # graph[0].setNewEdgeInVertex('AC', graph[2], 1)
    # graph[2].setNewEdgeInVertex('CB', graph[1], 1)
    # graph[1].setNewEdgeInVertex('BD', graph[3], 1)
    # graph[3].setNewEdgeInVertex('DC', graph[2], 1)
    # graph[2].setNewEdgeInVertex('CA', graph[0], 1)
    # graph[0].setNewEdgeInVertex('AB', graph[1], 1)
    # graph[1].setNewEdgeInVertex('BA', graph[0], 1)

    graph[0].setNewEdgeInVertex('AB', graph[1], 2)
    graph[1].setNewEdgeInVertex('BA', graph[0], 2)

    graph[0].setNewEdgeInVertex('AC', graph[2], 3)
    graph[2].setNewEdgeInVertex('AC', graph[0], 3)
    
    graph[0].setNewEdgeInVertex('AK', graph[10], 4)
    graph[10].setNewEdgeInVertex('KA', graph[0], 4)
    
    graph[0].setNewEdgeInVertex('AE', graph[4], 6)
    graph[4].setNewEdgeInVertex('EA', graph[0], 6)
    
    graph[4].setNewEdgeInVertex('EK', graph[10], 7)
    graph[10].setNewEdgeInVertex('KE', graph[4], 7)
    
    graph[7].setNewEdgeInVertex('HG', graph[6], 3)
    graph[6].setNewEdgeInVertex('GH', graph[7], 3)
    
    graph[2].setNewEdgeInVertex('CH', graph[7], 5)
    graph[7].setNewEdgeInVertex('HC', graph[2], 5)
    
    graph[6].setNewEdgeInVertex('GI', graph[8], 11)
    graph[8].setNewEdgeInVertex('IG', graph[6], 11)
    
    graph[8].setNewEdgeInVertex('IJ', graph[9], 3)
    graph[9].setNewEdgeInVertex('JI', graph[8], 3)
    
    graph[9].setNewEdgeInVertex('JH', graph[7], 2)
    graph[7].setNewEdgeInVertex('HJ', graph[9], 2)
    
    graph[6].setNewEdgeInVertex('GF', graph[5], 5)
    graph[5].setNewEdgeInVertex('FG', graph[6], 5)
    
    graph[5].setNewEdgeInVertex('FE', graph[4], 8)
    graph[4].setNewEdgeInVertex('EF', graph[5], 8)
    
    graph[5].setNewEdgeInVertex('FD', graph[3], 6)
    graph[3].setNewEdgeInVertex('DF', graph[5], 6)
    
    graph[3].setNewEdgeInVertex('DB', graph[1], 9)
    graph[1].setNewEdgeInVertex('BD', graph[3], 9)

    graph[6].setNewEdgeInVertex('GK', graph[10], 10)
    graph[10].setNewEdgeInVertex('KG', graph[6], 10)

    graph[10].setNewEdgeInVertex('KC', graph[2], 9)
    graph[2].setNewEdgeInVertex('CK', graph[10], 9)

    # if gp.verifyPath(graph[0], graph[3], edgesPassed): # A - D   
    #     print('\n-------- tem caminho ---------\n')
    #     print('{} <---> {}' .format(graph[0], graph[3]))        
    #     for edge in edgesPassed:
    #         print('{}' .format(edge))   
    # else:
    #     print('não tem caminho')
    
    # edgesPassed = []
    
    # if gp.verifyCicle(graph[0], graph[0]): 
    #     print('\n-------- é hamiltoniano ---------\n')
    #     gp.showPathHamilton(graph)

    # if gp.isEulerian(graph):
    #     print('\n-------- é euleriano ---------\n')
    #     gp.showPathEulerian(graph)
    # else:
    #     print('nao eh euleriano')

    # print('\n-------- busca largura ---------\n')
    # gp.buscaLargura(fila, graph, edgesPassed)

    # edgesPassed = []
    # fila = []

    # print('\n-------- busca profundidade ---------\n')
    # gp.buscaProfundidade(fila, graph, edgesPassed)    

    gp.shortPathDijkstra(graph[8], graph[10], graph)

# TODO
# a) uma função que dados 2 vértices como parâmetros, verifique se há caminho entre eles;

# b) outra função que dado um vértice (origem e tb destino), verifique se há um ciclo no grafo. Considere que para existir um 
#    ciclo deve sair de um vértice, visitar pelo menos outro vértice e, retornar ao vértice de origem.

# c) criar funçao pra verificar se é grafo euleriano e criar array com grafo

# d) hamilton

# e) busca por largura e busca por profundidade

# https://www.geeksforgeeks.org/euler-circuit-directed-graph/?ref=lbp 
