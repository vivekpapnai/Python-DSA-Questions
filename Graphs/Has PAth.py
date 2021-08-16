class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjacentMatrix = [[0 for j in range(nVertices)] for i in range(nVertices)]

    def addEdge(self, v1, v2):
        self.adjacentMatrix[v1][v2] = 1
        self.adjacentMatrix[v2][v1] = 1

    def removeEdge(self, v1, v2):
        self.adjacentMatrix[v1][v2] = 0
        self.adjacentMatrix[v2][v1] = 0

    def isContainEdge(self, v1, v2):
        if self.adjacentMatrix[v1][v2] == 1:
            return True
        return False

    def __dfsHelper(self, sv, visited):

        print(sv)
        visited[sv] = True
        for i in range(self.nVertices):
            if self.adjacentMatrix[sv][i] > 0 and visited[i] is False:
                self.__dfsHelper(i, visited)

    def dfs(self):
        visited = [False for i in range(self.nVertices)]
        self.__dfsHelper(0, visited)

    def __hasPathHelper(self, v1, v2, visited):
        if self.nVertices <= v2:
            return False
        if self.adjacentMatrix[v1][v2] > 0:
            return True
        visited[v1] = True
        for i in range(self.nVertices):
            if self.adjacentMatrix[v1][i] and visited[i] is False:
                if self.__hasPathHelper(i, v2, visited):
                    return True

        return False

    def hasPath(self, v1, v2):
        visited = [False for i in range(self.nVertices)]
        return self.__hasPathHelper(v1, v2, visited)


v, e = [int(i) for i in input().split()[:2]]
g = Graph(v)
for i in range(e):
    a, b = [int(x) for x in input().split()[:2]]
    g.addEdge(a, b)

v1, v2 = [int(r) for r in input().split()[:2]]
if g.hasPath(v1, v2):
    print("true")
else:
    print("false")
