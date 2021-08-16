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

    def __getMinVertex(self, visited, weight):
        min_vertex = -1
        for i in range(self.nVertices):
            if visited[i] is False and min_vertex == -1 or min_vertex > weight[i]:
                min_vertex = i
        return min_vertex

    def prims(self):
        visited = [False for i in range(self.nVertices)]
        parent = [-1 for i in range(self.nVertices)]
        weight = [sys.maxsize for i in range(self.nVertices)]
        weight[0] = 0
        for i in range(self.nVertices):
            min_vertex = self.__getMinVertex(visited, weight) # getting the minium weight vertex
            visited[i] = True # marking the edge as visited
            # exploring all the adjacent neighbours of min_vertex which is not visited
            # and update the weight corresponding to them if required
            for j in range(self.nVertices):
                if self.adjacentMatrix[min_vertex][j] > 0 and visited[j] is False:
                    if weight[j] > self.adjacentMatrix[min_vertex][j]:
                        weight[j] = self.adjacentMatrix[min_vertex][j]
                        parent[j] = min_vertex

        # printing the mst
        for i in range(1,self.nVertices):
            if i < parent[i]:
                print(str(i) + " " + str(parent[i]) + " " + str(weight[i]))
            else:
                print(str(parent[i]) + " " + str(i) + " " + str(weight[i]))


li = [int(x) for x in input().split()]
n = li[0]
e = li[1]  # total edges
g = Graph(n)
for i in range(e):
    curr_input = [int(ele) for ele in input().split()]
    g.addEdge(curr_input[0], curr_input[1], curr_input[2])
g.prims()
