import queue
import sys
sys.setrecursionlimit(10**6)

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

    def __allConnectedComp(self, sv, visited, list):
        list.append(sv)
        visited[sv] = True
        for i in range(self.nVertices):
            if self.adjacentMatrix[sv][i] and visited[i] is False:
                self.__allConnectedComp(i, visited, list)
        return list

    def allConnectedComp(self):
        visited = [False for i in range(self.nVertices)]
        list = []
        for i in range(self.nVertices):
            if visited[i] is False:
                li = self.__allConnectedComp(i, visited, [])
                list.append(li)
        return list


v, e = [int(i) for i in input().split()[:2]]
g = Graph(v)

for i in range(e):
    a, b = [int(x) for x in input().split()[:2]]
    g.addEdge(a, b)

list = g.allConnectedComp()
for i in list:
    i.sort()
    for j in i:
        print(j, end=" ")
    print()

