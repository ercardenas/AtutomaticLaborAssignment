#!/usr/bin/env python

class LaborGraph(object):
    """ A class to represent a bipartite graph

    This particular bipartite graph can be divided into two disjoint sets:
    - Halstead members: college students who are currently living in Halstead
    - Halstead labors: different types of work necessary to operate Halstead

    Attributes:
        adj: dict mapping from a halstead member to his possible labor, 
             or viceversa
        flow: dict mapping from an edge to its flow
    """

    def __init__(self):
        """Inits LaborGraph with empty values."""  
        self.adj = {}
        self.flow = {}

    def add_vertex(self, v):
        """Inits the adj dictionary for the new vertex.

        Args:
            v: vertex to represent either a halstead member or a halstead labor
        """
        self.adj[v] = []

    def get_adj_edges(self, v):
        """Get the adjacent edges of vertex v.

        Args:
            v: vertex to represent either a halstead member or a halstead labor

        Returns:
            A dict of the adjacent edges to vertex v.mapping from a halstead 
            member to his possible labor, or the other way around 
        """
        return self.adj[v]

    def add_edge(self, u, v, w=0):
        """Adds the given edge into LaborGraph class

        Args:
            u: string u that represents a halstead member
            v: string v that represents a halsead labor
            w: int that represents capacity

        Raises:
            Cannot add a self edge
        """ 
        if u == v:
            raise ValueError("u == v")
        edge = Edge(u,v,w)
        redge = Edge(v,u,0) # residual edge
        edge.redge = redge 
        redge.redge = edge
        self.adj[u].append(edge)
        self.adj[v].append(redge)
        self.flow[edge] = 0
        self.flow[redge] = 0

    def find_labor(self, member, labor, path, path_set):
        """Find the possible labor for a given member

        This is an augmented path used in the Ford-Fulkerson algorithm

        Args:
            member: string to represent a halstead member, source vertex
            labor: string to represent a halsead labor, sink vertex
            path: the current path, labor
            path_set: possible paths, labors

        Returns:
            An edge that represents a possible labor assignment, augmented path
        """ 
        if member == labor:
            return path
        for edge in self.get_adj_edges(member):
            residual = edge.capacity - self.flow[edge]
            if residual > 0 and not (edge,residual) in path_set:
                path_set.add((edge, residual))
                result = self.find_labor( edge.labor, labor, path 
                                          + [(edge,residual)], path_set)
                if result != None:
                    return result

    def labor_assignment(self, s, t, members):
        """Prints the final labor assignment for all members

        Runs a version of Ford-Fulkerson to find the labor assignment.
        Since LaborGraph is a bipartite graph, I need to add a source
        and sink vertices in order to run Ford-Fulkerson algorithm.

        Args:
            s: source temporal vertex
            t: sink temporal vertex
            members: list of all halstead members
        """ 
        path = self.find_labor(s, t, [], set())
        while path != None:
            flow = min(res for edge,res in path)
            for edge,res in path:
                self.flow[edge] += flow
                self.flow[edge.redge] -= flow
            path = self.find_labor(s, t, [], set())

        # Print the final labor assignment
        for member in members:
            for edge in self.get_adj_edges(member):
                if self.flow[edge] == 1:
                    print edge

    class Edge(object):
        """ A class to represent an edge in LaborGraph class

        The edge(u,v) represents if a halstead member 'u' is available
        to do labor 'v'

        Attributes:
            member: tail of the edge, a string to represent a halstead member
            labor: head of the edge, a string to represent a hastead labor
            capacity: integer to be used in the labor_assignment function
        """

        def __init__(self, u, v, w):
            """Inits Edge with the given values

            Args:
                u: string u that represents a halstead member
                v: string v that represents a halsead labor
                w: int that represents capacity
            """  
            self.member = u
            self.labor = v
            self.capacity = w

        def __repr__(self):
            """ Prints the assignment from the member to its labor.

            Returns:
                String representing edge(u,v) as u->v
            """
            return "%s->%s" % (self.member, self.labor)


