import queue


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

    def __bfsHelper(self, sv, visited):
        q = queue.Queue()
        q.put(sv)
        visited[sv] = True
        while q.empty() is not True:
            ele = q.get()
            print(ele)
            # visited[ele] = True
            for i in range(self.nVertices):
                if self.adjacentMatrix[ele][i] > 0 and visited[i] is False:
                    q.put(i)
                    visited[i] = True

    def bfs(self):
        visited = [False for i in range(self.nVertices)]
        for i in range(self.nVertices):
            if visited[i] is False:
                self.__bfsHelper(i, visited)


g = Graph(5)
g.addEdge(0, 1)
g.addEdge(1, 2)
# g.addEdge(2, 3)
g.addEdge(0, 2)
g.addEdge(3, 4)
g.bfs()
