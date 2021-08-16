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

    def __getPathHelper(self, sv, ev, visited):
        q = queue.Queue()
        q.put(sv)
        visited[sv] = True
        parent_dict = {}
        li = []
        x = sv
        while q.empty() is False:
            ele = q.get()
            for i in range(self.nVertices):
                if self.adjacentMatrix[ele][i] > 0 and visited[i] is False:
                    if i == ev:
                        li.append(i)
                        visited[i] = True
                        parent_dict[i] = ele
                        x = i
                        break
                    q.put(i)
                    parent_dict[i] = ele
                    visited[i] = True
        while x != sv:
            li.append(parent_dict[x])
            x = parent_dict[x]

        return li

    def getPath(self, sv, ev):
        visited = [False for i in range(self.nVertices)]
        return self.__getPathHelper(sv, ev, visited)


v, e = [int(i) for i in input().split()[:2]]
g = Graph(v)
for i in range(e):
    a, b = [int(x) for x in input().split()[:2]]
    g.addEdge(a, b)

v1, v2 = [int(r) for r in input().split()[:2]]
ans = g.getPath(v1, v2)
if ans is not None:
    for i in ans:
        print(i, end=" ")
