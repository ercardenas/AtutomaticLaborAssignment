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
	while path != 	None:
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
	for name in ['Erick', 'Raul']:
		for edge in G.get_edges(name):
			# if visited[v] and not visited[edge.sink] and edge.capacity > 0:
			if G.flow[edge] == 1:
				print name, ' - ', edge.sink

g = Graph()
map(g.add_vertex, ['s', 't', 'Erick', 'Raul', 'Dinner Cooking', 'Lunch Cooking'])
g.add_edge('s', 'Raul', 1)
g.add_edge('s', 'Erick', 1)
g.add_edge('Raul', 'Lunch Cooking', 2)
g.add_edge('Erick', 'Dinner Cooking', 2)
g.add_edge('Erick', 'Lunch Cooking', 2)
g.add_edge('Lunch Cooking', 't', 1)
g.add_edge('Dinner Cooking', 't', 1)
min_st_edge_cut(g, 's', 't')


for name in names:
	for answer in answers:
	g.add_edge(name, labor[answer['row']][answer['col']], 2)


labor = {   u'9275058246': {   u'9275058263': 0,    # Mon     6 - 7 am
        	    	           u'9275058264': 0,	# Tues	
            	    	       u'9275058265': 0,	# Wed
                	    	   u'9275058266': 0,	# Thurs
	                	       u'9275058268': 0,	# Fri
    	                	   u'9275058269': 0,	# Sat
        	            	   u'9275058270': 0},	# Sun
    		u'9275058247': {   u'9275058263': 0,	# Mon     7 - 8 am
        	    	           u'9275058264': 0,	# Tues	
            	    	       u'9275058265': 0,	# Wed
                	    	   u'9275058266': 0,	# Thurs
	                	       u'9275058268': 0,	# Fri
    	                	   u'9275058269': 0,	# Sat
        	            	   u'9275058270': 0},	# Sun
		    u'9275058248': {   u'9275058263': "Mon - Morning Hobbit",	# Mon     8 - 9 am
        	    	           u'9275058264': "Tues - Morning Hobbit",	# Tues	
            	    	       u'9275058265': "Wed - Morning Hobbit",	# Wed
                	    	   u'9275058266': "Thurs - Morning Hobbit",	# Thurs
	                	       u'9275058268': "Fri - Morning Hobbit",	# Fri
    	                	   u'9275058269': 0,	# Sat
        	            	   u'9275058270': 0},	# Sun
		    u'9275058249': {   u'9275058263': "Mon - Lunch Cook",	# Mon     9 - 10 am
        	    	           u'9275058264': "Tues - Lunch Cook",	# Tues	
            	    	       u'9275058265': "Wes - Lunch Cook",	# Wed
                	    	   u'9275058266': "Thurs - Lunch Cook",	# Thurs
	                	       u'9275058268': "Fri - Lunch Cook",	# Fri
    	                	   u'9275058269': "Sat - Morning Hobbit",	# Sat
        	            	   u'9275058270': "Sun - Morning Hobbit"},	# Sun
		    u'9275058250': {   u'9275058263': "Mon - Lunch Cook",	# Mon     10 - 11 am
        	    	           u'9275058264': "Tues - Lunch Cook",	# Tues	
            	    	       u'9275058265': "Wes - Lunch Cook",	# Wed
                	    	   u'9275058266': "Thurs - Lunch Cook",	# Thurs
	                	       u'9275058268': "Fri - Lunch Cook",	# Fri
    	                	   u'9275058269': 0,	# Sat
        	            	   u'9275058270': 0},	# Sun
		    u'9275058251': {   u'9275058263': 0,	# Mon     11 am - 12 pm
        	    	           u'9275058264': 0,	# Tues	
            	    	       u'9275058265': 0,	# Wed
                	    	   u'9275058266': 0,	# Thurs
	                	       u'9275058268': 0,	# Fri
    	                	   u'9275058269': 0,	# Sat
        	            	   u'9275058270': 0},	# Sun
		    u'9275058252': {   u'9275058263': "Mon - Lunch Clean",	# Mon     12 - 1 pm
        	    	           u'9275058264': "Tues - Lunch Clean",	# Tues	
            	    	       u'9275058265': "Wed - Lunch Clean",	# Wed
                	    	   u'9275058266': "Thurs - Lunch Clean",	# Thurs
	                	       u'9275058268': "Fri - Lunch Clean",	# Fri
    	                	   u'9275058269': 0,	# Sat
        	            	   u'9275058270': 0},	# Sun
		    u'9275058253': {   u'9275058263': "Mon - Lunch Clean",	# Mon     1 - 2 pm
        	    	           u'9275058264': "Tues - Lunch Clean",	# Tues	
            	    	       u'9275058265': "Wed - Lunch Clean",	# Wed
                	    	   u'9275058266': "Thurs - Lunch Clean",	# Thurs
	                	       u'9275058268': "Fri - Lunch Clean",	# Fri
    	                	   u'9275058269': 0,	# Sat
        	            	   u'9275058270': 0},	# Sun
		    u'9275058254': {   u'9275058263': "Mon - Dinner Cook",	# Mon     2 - 3 pm
        	    	           u'9275058264': "Tues - Dinner Cook",	# Tues	
            	    	       u'9275058265': "Wed - Dinner Cook",	# Wed
                	    	   u'9275058266': "Thurs - Dinner Cook",	# Thurs
	                	       u'9275058268': "Fri - Dinner Cook",	# Fri
    	                	   u'9275058269': 0,	# Sat
        	            	   u'9275058270': 0},	# Sun
		    u'9275058255': {   u'9275058263': "Mon - Dinner Cook",	# Mon     3 - 4 pm
        	    	           u'9275058264': "Tues - Dinner Cook",	# Tues	
            	    	       u'9275058265': "Wed - Dinner Cook",	# Wed
                	    	   u'9275058266': "Thurs - Dinner Cook",	# Thurs
	                	       u'9275058268': "Fri - Dinner Cook",	# Fri
    	                	   u'9275058269': 0,	# Sat
        	            	   u'9275058270': 0},	# Sun
		    u'9275058256': {   u'9275058263': "Mon - Dinner Cook",	# Mon     4 - 5 pm
        	    	           u'9275058264': "Tues - Dinner Cook",	# Tues	
            	    	       u'9275058265': "Wed - Dinner Cook",	# Wed
                	    	   u'9275058266': "Thurs - Dinner Cook",	# Thurs
	                	       u'9275058268': "Fri - Dinner Cook",	# Fri
    	                	   u'9275058269': 0,	# Sat
        	            	   u'9275058270': 0},	# Sun
		    u'9275058257': {   u'9275058263': "Mon - Dinner Cook",	# Mon     5 - 6 pm
        	    	           u'9275058264': "Tues - Dinner Cook",	# Tues	
            	    	       u'9275058265': "Wed - Dinner Cook",	# Wed
                	    	   u'9275058266': "Thurs - Dinner Cook",	# Thurs
	                	       u'9275058268': "Fri - Dinner Cook",	# Fri
    	                	   u'9275058269': 0,	# Sat
        	            	   u'9275058270': 0},	# Sun
		    u'9275058258': {   u'9275058263': 0,	# Mon     6 - 7 pm
        	    	           u'9275058264': 0,	# Tues	
            	    	       u'9275058265': 0,	# Wed
                	    	   u'9275058266': 0,	# Thurs
	                	       u'9275058268': 0,	# Fri
    	                	   u'9275058269': 0,	# Sat
        	            	   u'9275058270': 0},	# Sun
		    u'9275058259': {   u'9275058263': "Mon - Dinner Clean",	# Mon     7 - 8 pm
        	    	           u'9275058264': "Tues - Dinner Clean",	# Tues	
            	    	       u'9275058265': "Wed - Dinner Clean",	# Wed
                	    	   u'9275058266': "Thurs - Dinner Clean",	# Thurs
	                	       u'9275058268': "Fri - Dinner Clean",	# Fri
    	                	   u'9275058269': 0,	# Sat
        	            	   u'9275058270': 0},	# Sun
		    u'9275058260': {   u'9275058263': "Mon - Dinner Clean",	# Mon     8 - 9 pm
        	    	           u'9275058264': "Tues - Dinner Clean",	# Tues	
            	    	       u'9275058265': "Wed - Dinner Clean",	# Wed
                	    	   u'9275058266': "Thurs - Dinner Clean",	# Thurs
	                	       u'9275058268': "Fri - Dinner Clean",	# Fri
    	                	   u'9275058269': 0,	# Sat
        	            	   u'9275058270': 0},	# Sun
		    u'9275058261': {   u'9275058263': 0,	# Mon     9 - 10 pm
        	    	           u'9275058264': 0,	# Tues	
            	    	       u'9275058265': 0,	# Wed
                	    	   u'9275058266': 0,	# Thurs
	                	       u'9275058268': 0,	# Fri
    	                	   u'9275058269': 0,	# Sat
        	            	   u'9275058270': 0},	# Sun
		    u'9275058262': {   u'9275058263': 0,	# Mon     10 - 11 pm
        	    	           u'9275058264': 0,	# Tues	
            	    	       u'9275058265': 0,	# Wed
                	    	   u'9275058266': 0,	# Thurs
	                	       u'9275058268': 0,	# Fri
    	                	   u'9275058269': 0,	# Sat
        	            	   u'9275058270': 0},	# Sun
