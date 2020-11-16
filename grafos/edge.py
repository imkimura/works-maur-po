class Edge:
    def __init__(self, edgeName, vertexDestiny, cost):        
        self.edgeName = edgeName
        self.vertexDestiny = vertexDestiny
        self.cost = cost

    def getEdge(self):
        return self.edgeName

    def __str__(self):
        return '{}' .format(self.edgeName)