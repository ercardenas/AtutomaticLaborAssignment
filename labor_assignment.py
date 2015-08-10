#!/usr/bin/python

from LaborGraph import LaborGraph
from polling import polling
from labor_map import labor_map, labors_list

output_response_list = polling()

members_names = []
for response in output_response_list:
	members_names.append(response['questions'][0]['answers'][0]['text'])

g = LaborGraph()
map(g.add_vertex, ['s', 't'])
map(g.add_vertex, members_names) 
for labor in labors_list:
    g.add_vertex(labor[0]) 

for response in output_response_list:
    member = response['questions'][0]['answers'][0]['text']
    g.add_edge('s', member, 4)
    for answer in response['questions'][1]['answers']:
        labor = labor_map[answer['row']][answer['col']]
        if(labor != 0):
            g.add_edge(member, labor, 2)

for labor in labors_list:
    g.add_edge(labor[0], 't', labor[1])

g.labor_assignment('s', 't',members_names)   