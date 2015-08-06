#!/usr/bin/env python

class Edge(object):
	def __init__(self, u, v, w):
		self.source = u
		self.sink = v
		self.capacity = w

	def __repr__(self):
		return "%s->%s:%s" % (self.source, self.sink, self.capacity)

class Graph(object):
	def __init__(self):
		self.adj = {}
		self.flow = {}
		self.vertex_set = set()

	def add_vertex(self, vertex):
		self.adj[vertex] = []
		self.vertex_set.add(vertex)

	def get_edges(self, v):
		return self.adj[v]

	def add_edge(self, u, v, w=0):
		if u == v:
			raise ValueError("u == v")
		edge = Edge(u,v,w)
		redge = Edge(v,u,0)
		edge.redge = redge #redge is not defined in Edge class
		redge.redge = edge
		self.adj[u].append(edge)
		self.adj[v].append(redge)
		self.flow[edge] = 0
		self.flow[redge] = 0

	def find_path(self, source, sink, path, path_set):
		if source == sink:
			return path
		for edge in self.get_edges(source):
			residual = edge.capacity - self.flow[edge]
			if residual > 0 and not (edge,residual) in path_set:
				path_set.add((edge, residual))
				result = self.find_path( edge.sink, sink, path + [(edge,residual)], path_set)
				if result != None:
					return result

def dfs(G, s, visited):
    visited[s] = True;
    for edge in G.get_edges(s):
    	residual = edge.capacity - G.flow[edge]
    	if (residual > 0 and not visited[edge.sink]):
           dfs(G, edge.sink, visited)


def min_st_edge_cut(G, s, t):
	path = G.find_path(s, t, [], set())
	while path != None:
		flow = min(res for edge,res in path)
		for edge,res in path:
			G.flow[edge] += flow
			G.flow[edge.redge] -= flow
		path = G.find_path(s, t, [], set())
	
	# Flow is maximum now, find vertices reachable from s
	visited = {}.fromkeys(G.vertex_set, False)
	dfs(G, s, visited)

    # Print all edges that are from a reachable vertex to
    # non-reachable vertex in the original graph
	for v in G.vertex_set:
		for edge in G.get_edges(v):
			if visited[v] and not visited[edge.sink] and edge.capacity > 0:
				print v, ' - ', edge.sink

g = Graph()
map(g.add_vertex, ['0', '1', '2', '3', '4', '5'])
g.add_edge('0', '1', 16)
g.add_edge('0', '2', 13)
g.add_edge('1', '2', 10)
g.add_edge('1', '3', 12)
g.add_edge('2', '4', 14)
g.add_edge('2', '1', 4)
g.add_edge('3', '2', 9)
g.add_edge('3', '5', 20)
g.add_edge('4', '3', 7)
g.add_edge('4', '5', 4)
min_st_edge_cut(g, '0', '5')

