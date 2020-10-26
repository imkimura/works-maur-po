class Edge:
    def __init__(self, edgeName, vertexDestiny):        
        self.edgeName = edgeName
        self.vertexDestiny = vertexDestiny

    def getEdge(self):
        return self.edgeName

    def __str__(self):
        return '{} - Aresta' .format(self.edgeName)