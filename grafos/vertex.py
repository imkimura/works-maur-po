from edge import Edge


class Vertex:
    def __init__(self, vertexName):
        self.vertexName = vertexName
        self.edges = []
        self.edgesIN = []
    
    def __str__(self):
        return '{}' .format(self.vertexName)
    
    def setNewEdgeInVertex(self, edgeName, destiny):
        edge = Edge(edgeName, destiny)
        
        destiny.edgesIN.append(self)
        
        self.edges.append(edge)    
