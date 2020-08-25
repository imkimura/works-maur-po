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

    

