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
        for i in range(self.nVertices):
            if visited[i] is False:
                self.__dfsHelper(i, visited)

    def __isConnectedHelper(self, sv, visited):
        visited[sv] = True
        for i in range(self.nVertices):
            if self.adjacentMatrix[sv][i] > 0 and visited[i] is False:
                self.__isConnectedHelper(i, visited)
        return visited

    def isConnected(self, sv):
        if self.nVertices == 0:
            return [True]
        visited = [False for i in range(self.nVertices)]
        return self.__isConnectedHelper(sv, visited)


v, e = [int(x) for x in input().split()[:2]]
g = Graph(v)
for i in range(e):
    a, b = [int(x) for x in input().split()[:2]]
    g.addEdge(a, b)
visited = g.isConnected(0)
Flag = True
for i in visited:
    if i is False:
        Flag = False
if Flag:
    print('true')
else:
    print('false')