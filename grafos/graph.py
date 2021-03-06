from edge import Edge
from vertex import Vertex
from random import randint


def verifyPath(orign, destiny, edgesPassed):
    
    if len(orign.edges) == 0:
        return False

    for edge in orign.edges:
        if len(edgesPassed) > 0:
            if edge not in edgesPassed:               
                edgesPassed.append(edge)
            else:
                return False
        else:
            edgesPassed.append(edge)

        if edge.vertexDestiny == destiny:            
            return True
        else:                     
            if verifyPath(edge.vertexDestiny, destiny, edgesPassed):
                return True
    return False

def verifyCicle(orign, destiny):
    
    if len(orign.edges) == 0:
        print('deu ruim')
        return False

    edgesPassed = []
    if verifyPath(orign, destiny, edgesPassed):
        edgesPassed = []
        if verifyPath(destiny, orign, edgesPassed):                        
            return True            
    return False

def isEulerian(graph): 

    for i in range(len(graph)): 
        if len(graph[i].edges) == len(graph[i].edgesIN):
            if (len(graph[i].edges) + len(graph[i].edgesIN)) % 2 != 0: #verifica se algum vertice tem grau impar mas precisar ver quantas arestas tem em um vertice
                return False
        else:
            return False
    return True

def showPathEulerian(graph):
    tour=[]
    tourEulerian(graph[0], tour)
    
def tourEulerian(vertex, tour):
    if len(vertex.edges) > 0:
        for edge in vertex.edges:      
            if edge not in tour:
                tour.append(edge)        
                print(f'{vertex} -- {edge} -> {edge.vertexDestiny}')            
                tourEulerian(edge.vertexDestiny, tour)                
        return True
    else:
        return False

def showPathHamilton(graph):
    tour=[]
    tourHamilton(graph[0], tour)    
    
def tourHamilton(vertex, tour):
    if len(vertex.edges) > 0:
        for edge in vertex.edges:      
            if vertex not in tour:
                tour.append(vertex)        
                print(f'{vertex} -- {edge} -> {edge.vertexDestiny}')            
                tourHamilton(edge.vertexDestiny, tour)                
        return True
    else:
        return False

def getFirstVertex(fila):
    first = fila[0]
    fila.remove(first)
    return first, fila

def getLastVertex(fila):
    last = fila[len(fila)-1]
    fila.pop()
    return last, fila

def sucessor(vertex, fila, edgesPassed):
    if len(vertex.edges) > 0:
        for edge in vertex.edges:
            if edge.vertexDestiny not in fila and edge.vertexDestiny not in edgesPassed:
                fila.append(edge.vertexDestiny)
                edgesPassed.append(edge.vertexDestiny)
    return fila, edgesPassed

def buscaLargura(fila, graph, edgesPassed):
    fila.append(graph[0])
    edgesPassed.append(graph[0])   

    count = 0

    while(len(fila) > 0):
        
        vertex, fila = getFirstVertex(fila)
        print(vertex)
                
        fila, edgesPassed = sucessor(vertex, fila, edgesPassed)

        count += 1

def buscaProfundidade(fila, graph, edgesPassed):
    fila.append(graph[0])
    edgesPassed.append(graph[0])   

    count = 0
    
    while(len(fila) > 0):
        
        vertex, fila = getLastVertex(fila)
        print(vertex)
                
        fila, edgesPassed = sucessor(vertex, fila, edgesPassed)

        count += 1

def shortPathDijkstra(start, destiny, graph):
    vertex = start
    
    markedVertex = []
    previous = [None] * len(graph)
    accumulatedDistances = [float('inf')] * len(graph)     
    
    while(verifyPathFound(vertex, destiny)):
        
        previous, accumulatedDistances, markedVertex = exploreVertex(vertex, previous, accumulatedDistances, markedVertex, graph)
        
        vertex = nextVertexExplore(accumulatedDistances, markedVertex, graph)
    
    printPathDijkstra(accumulatedDistances, previous, graph, graph.index(destiny))
    print(' [FIM]')

def printPathDijkstra(accumulatedDistances, previous, graph, index):
    
    if previous[index] is None:
        print('\n\n             ↓ Melhor caminho ↓ \n')
        print('{:^5} ->' .format(graph[index].vertexName), end=" ")
        return True
    
    prevIndex = index
    
    for indexV, vertex in enumerate(graph):        
        if vertex.vertexName == previous[index]:            
            index = indexV
            break
            
    printPathDijkstra(accumulatedDistances, previous, graph, index)
    
    print(' {:^5}♦{:^4} ' .format(graph[prevIndex].vertexName, accumulatedDistances[prevIndex]), end="->")

    return True
    
    

def verifyPathFound(vertex, destiny):    
    if vertex == destiny:
        return False
    else: 
        return True

def nextVertexExplore(accumulatedDistances, markedVertex, graph):
    minValue = float('inf')
    
    for idx, distance in enumerate(accumulatedDistances):
        if (distance < minValue) and (graph[idx] not in markedVertex):
            minValue = distance
            vertex = graph[idx]
            
    return vertex

def exploreVertex(vertex, previous, accumulatedDistances, markedVertex, graph):    
    print(f'\n------------ \niniciando função com {vertex.vertexName}...\n')
        
    idxVertex = graph.index(vertex)
    
    for edge in vertex.edges:
        idxVertexDestiny = graph.index(edge.vertexDestiny)
        
        if edge.vertexDestiny in markedVertex:
            pass
        else:
            sumPrevious = accumulatedDistances[idxVertex]
            
            if accumulatedDistances[idxVertex] == float('inf') : sumPrevious = 0
            
            sumCost = edge.cost + sumPrevious
            
            if accumulatedDistances[idxVertexDestiny] > (sumCost):

                accumulatedDistances[idxVertexDestiny] = sumCost
                previous[idxVertexDestiny] = vertex.vertexName            

        markedVertex.append(vertex)    
           
    return previous, accumulatedDistances, markedVertex
    
    