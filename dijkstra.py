class Vertex():
    def __init__(self, node):
        self.value = node
        self.adjacent = {}

    def addNeighbor(self, neighbor, weight):
        self.adjacent[neighbor] = weight

    def getNeighbors(self):
        return self.adjacent 

    def getValue(self):
        return self.value

    def getWeight(self, neighbor):
        return self.adjacent[neighbor]

class Graph():
    def __init__(self):
        self.vertices = {}
        self.number_vertices = 0

    def __iter__(self):
        return iter(self.vertices.values())

    def addVertex(self, node):
        self.number_vertices = self.number_vertices + 1
        new_vertex = Vertex(node)
        self.vertices[node] = new_vertex
        return new_vertex

    def getVertex(self, n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def addEdge(self, start, end, weight):
        if start not in self.vertices:
            self.addVertex(start)
        if end not in self.vertices:
            self.addVertex(end)

        self.vertices[start].addNeighbor(self.vertices[end], weight)
        self.vertices[end].addNeighbor(self.vertices[start], weight)

    def getVertices(self):
        return self.vertices.keys()

def dijkstra(graph, source):
	dist = {}
	Q = []
	dist[source] = 0

	for v in graph:
		if v.getValue() != source.getValue():
			dist[v] = float("inf")	
		Q.append(v)
			
	while Q != []:
		x = float("inf")
		y = None
		for v in Q:
			if dist[v] < x:
				x = dist[v]
				y = v
		Q.remove(y)		

		for w in y.getNeighbors():
			if w in Q:
				alt = dist[y] + y.getWeight(w)
				if alt < dist[w]:
					dist[w] = alt

	for v in dist:
		print(v.getValue(), dist[v])

g = Graph()

z = g.addVertex('s')
g.addVertex('a')
g.addVertex('b')
g.addVertex('c')
g.addVertex('d')
g.addVertex('e')
g.addVertex('f')

g.addEdge('s', 'a', 3)  
g.addEdge('s', 'c', 2)
g.addEdge('s', 'f', 6)
g.addEdge('a', 'c', 2)
g.addEdge('a', 'b', 6)
g.addEdge('a', 'd', 1)
g.addEdge('b', 'e', 1)
g.addEdge('c', 'd', 3)
g.addEdge('d', 'e', 4)
g.addEdge('e', 'f', 2)

for v in g:
    for w in v.getNeighbors().keys():
        vvalue = v.getValue()
        wvalue = w.getValue()
        print '( %s -> %s, %d)'  % ( vvalue, wvalue, v.getWeight(w))

print (dijkstra(g, z))
