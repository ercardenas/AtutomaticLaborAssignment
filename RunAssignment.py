#!/usr/bin/env python

from LaborAssignment import FlowNetwork

g = FlowNetwork()
map(g.add_vertex, ['s', 'o', 'p', 'q', 'r', 't'])
g.add_edge('s', 'o')
g.add_edge('s', 'p')
g.add_edge('o', 'p')
g.add_edge('o', 'q')
g.add_edge('p', 'r')
g.add_edge('r', 't')
g.add_edge('q', 'r')
g.add_edge('q', 't')
print g.max_flow('s', 't')
