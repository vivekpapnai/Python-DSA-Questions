class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjMat = [[0 for j in range(nVertices)] for i in range(nVertices)]

    def addEdge(self, v1, v2):
        self.adjMat[v1][v2] = 1
        self.adjMat[v2][v1] = 1

    def removeEdge(self, v1, v2):
        if self.isContainsEdge(v1, v2) is False:
            return
        self.adjMat[v1][v2] = 0
        self.adjMat[v2][v1] = 0

    def isContainsEdge(self, v1, v2):
        # return True if self.adjMat[v1][v2] > 0 else False
        if self.adjMat[v1][v2] > 0:
            return True
        else:
            return False

    def __str__(self):
        return str(self.adjMat)


g = Graph(5)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 3)
print(g)
