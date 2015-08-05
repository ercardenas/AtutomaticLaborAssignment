#!/usr/bin/env python

g = FlowNetwork()
map(g.AddVertex, ['s', 'o', 'p', 'q', 'r', 't'])
g.AddEdge('s', 'o')
g.AddEdge('s', 'p')
g.AddEdge('o', 'p')
g.AddEdge('o', 'q')
g.AddEdge('p', 'r')
g.AddEdge('r', 't')
g.AddEdge('q', 'r')
g.AddEdge('q', 't')
print g.MaxFlow('s', 't')
