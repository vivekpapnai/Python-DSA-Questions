"""
Kruskal algo says that to find the mst of a given tree start travelling the nodes with minium weight first and does not form cycle

to detect cycle: we can using has_path if the src and dest have already a path then it will form a cycle but it wil give v^2 time complexity:
- we can use union find algorithm to detect cycle :
    > create a parent array initalise to the self src:
    >  if parent of src_edge and dest_edge is different then it will not form a cycle add that edge in the output
        and change parent of either src_edge to dest_edge or dest_edge to src_edge.


Steps:
1: create a class Edge for takng input for a graph
2: sort the Edges array on basis of weight
3: to form mst no of edges should be (total_vertices -1) and to count it we will have a variable count=0\
4: while count < total_vertices -1
    - check if the src edge and destination edge form a cycle:

"""

"""
class Edge:
    def __init__(self, src, dest, wt):
        self.src = src
        self.dest = dest
        self.wt = wt


def getParent(v, parent):
    if v == parent[v]:
        return v
    return getParent(parent[v], parent)


def kruskal(edges, nvertices):
    parent = [i for i in range(nvertices)]
    edges = sorted(edges, key=lambda edge: edge.wt)
    count = 0
    output = []
    i = 0
    while count < (nvertices - 1):
        currEdge = edges[i]
        srcParent = getParent(currEdge.src, parent)
        destParent = getParent(currEdge.dest, parent)

        if srcParent != destParent:
            output.append(currEdge)
            count += 1
            parent[srcParent] = destParent
        i += 1
    return output


li = [int(x) for x in input().split()]
n = li[0]
e = li[1]  # total edges
edges = []
for i in range(e):
    curr_input = [int(ele) for ele in input().split()]
    src = curr_input[0]
    dest = curr_input[1]
    wt = curr_input[2]
    edge = Edge(src, dest, wt)
    edges.append(edge)
output = kruskal(edges, n)
for currEdge in output:
    if currEdge.src < currEdge.dest:
        print(str(currEdge.src) + " " + str(currEdge.dest) + " " + str(currEdge.wt))
    else:
        print(str(currEdge.dest) + " " + str(currEdge.src) + " " + str(currEdge.wt))
"""

""" 
    Time complexity will be: 
    (ElogE) for sorting the edges 
    (EV) for traversing al of the vertices to form mst (E to traverse all of the vertices and V for finding the parent)
    so total time complexity will be : (ElogE + EV)
    
    We can use another algorithm to optimise our solution using "Union by rank and path compression" algorithm 
    it states that the subest which is has smallar rank/size merge it with the larger rank/size subset and if they are equal 
    then make any of them the parent and increase the rank by 1
    it has logV complexity
    so total complexity of kruskal using union by rank and path compression is : (ElogE + ElogV)
"""


class Edge:
    def __init__(self, src, dest, wt):
        self.src = src
        self.dest = dest
        self.wt = wt


class subset:
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank


def getParent(v, parent):
    if v == parent[v]:
        return v
    return getParent(parent[v], parent)


def union(s, d, parent, rank):
    if rank[s] > rank[d]:
        parent[s] = d
    elif rank[s] < rank[d]:
        parent[d] = s
    else:
        parent[s] = d
        rank[d] += 1


def kruskal(edge, nvertices):
    parent = [i for i in range(nvertices)]
    rank = [0 for i in range(nvertices)]
    edge = sorted(edge, key=lambda edge: edge.wt)
    output = []
    count = 0
    i = 0
    while count < nvertices - 1:
        currEdge = edge[i]
        srcParent = getParent(currEdge.src, parent)
        destParent = getParent(currEdge.dest, parent)
        if srcParent != destParent:
            output.append(currEdge)
            count += 1
            union(srcParent, destParent, parent, rank)
        i += 1

    return output


li = [int(x) for x in input().split()]
n = li[0]
e = li[1]  # total edges
edges = []
for i in range(e):
    curr_input = [int(ele) for ele in input().split()]
    src = curr_input[0]
    dest = curr_input[1]
    wt = curr_input[2]
    edge = Edge(src, dest, wt)
    edges.append(edge)
output = kruskal(edges, n)
for currEdge in output:
    if currEdge.src < currEdge.dest:
        print(str(currEdge.src) + " " + str(currEdge.dest) + " " + str(currEdge.wt))
    else:
        print(str(currEdge.dest) + " " + str(currEdge.src) + " " + str(currEdge.wt))
