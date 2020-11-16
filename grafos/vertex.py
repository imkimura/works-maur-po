from edge import Edge


class Vertex:
    def __init__(self, vertexName):
        self.vertexName = vertexName
        self.edges = []
        self.edgesIN = []
    
    def __str__(self):
        return '{}' .format(self.vertexName)
    
    def setNewEdgeInVertex(self, edgeName, destiny, cost):
        edge = Edge(edgeName, destiny, cost)
        
        destiny.edgesIN.append(self)
        
        self.edges.append(edge)    
