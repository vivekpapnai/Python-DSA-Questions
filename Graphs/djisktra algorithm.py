import sys

class Graph:
    def __init__(self, nVertices):
        self.nVertices = nVertices
        self.adjacentMatrix = [[0 for j in range(nVertices)] for i in range(nVertices)]

    def addEdge(self, v1, v2, wt):
        self.adjacentMatrix[v1][v2] = wt
        self.adjacentMatrix[v2][v1] = wt

    def removeEdge(self, v1, v2):
        self.adjacentMatrix[v1][v2] = 0
        self.adjacentMatrix[v2][v1] = 0

    def isContainEdge(self, v1, v2):
        if self.adjacentMatrix[v1][v2] == 1:
            return True
        return False

    def __minDistance(self,visited, Distance):
        min_distance = -1
        for i in range(self.nVertices):
            if visited[i] is False and (min_distance == -1 or Distance[min_distance] > Distance[i]):
                min_distance = i
        return min_distance

    def djisktra(self):
        visited = [False for i in range(self.nVertices)]
        Distance = [sys.maxsize for i in range(self.nVertices)]
        # parent = [-1 for i in range(self.nVertices)]
        Distance[0] = 0
        for i in range(self.nVertices-1):
            min_distance = self.__minDistance(visited,Distance)
            visited[min_distance] = True
            for j in range(self.nVertices):
                if self.adjacentMatrix[min_distance][j] > 0 and visited[j] is False:
                    currW = Distance[min_distance] + self.adjacentMatrix[min_distance][j]
                    if Distance[j] > currW:
                        Distance[j] = currW

        for i in range(self.nVertices):
            print(i, Distance[i])


li = [int(x) for x in input().split()]
n = li[0]
e = li[1]  # total edges
g = Graph(n)
for i in range(e):
    curr_input = [int(ele) for ele in input().split()]
    g.addEdge(curr_input[0], curr_input[1], curr_input[2])
g.djisktra()