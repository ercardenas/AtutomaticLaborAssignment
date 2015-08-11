#!/usr/bin/python

from LaborGraph import LaborGraph
from polling import polling
from constants import LABOR_MAP, LABORS_LIST

__author__ = "Erick Cardenas"
__email__ = "ecardenas@utexas.edu"


def main():
	"""Automatic assigns labor to Halstead members

	Automatic assigns the required labor to Halstead members based on 
	their availability, which are collected through the following survey:
	https://www.surveymonkey.com/r/Y8Z7YTF

	The algorithm is a modified version of Ford-Fulkerson's algorithm. 
	First, the script creates a labor bipartite graph with two disjoint 
	sets: Halstead members and Halstead labors. Then, a source vertex is 
	added, which has an edge with every single Halstead member. Similarly,
	a sink vertex is added, which has an edge with every single Halstead
	labors. Then, the modified version of Ford-Fulkerson's algorithm is run.
	The labor assignment will be the edges that has a flow of one, ignoring
	the edges of the source and sink vertices.
	""" 
	# extracts members availability from surverys
	survey_response_list = polling()

	members_names = collect_members_names(survey_response_list)

	g = LaborGraph()

	# Adds source, vertex, members and labors to the graph
	add_vertices(g, members_names)

	# Creates the edges between members and their compatible labors
	# based on their availability
	add_edges(g, survey_response_list)

	# Runs modified version of Ford-Fulkerson's algorithm to
	# assign labors
	g.labor_assignment('s', 't',members_names)   

def collect_members_names(survey_response_list):
	""" Collects the members names from the answers of the surverys

	Args:
		survey_response_list: list that contains answers of the surverys

	Returns:
		A list containing the members names
	"""
	members_names = []
	for response in survey_response_list:
		members_names.append(response['questions'][0]['answers'][0]['text'])
	return members_names

def add_vertices(g, members_names):
	""" Adds vertices to labor graph: source, vertex, members and labors

	Args:
		g: LaborGraph object
		members_names: list containing members names
	"""
	map(g.add_vertex, ['s', 't'])
	map(g.add_vertex, members_names) 
	for labor in LABORS_LIST:
	    g.add_vertex(labor[0]) 

def add_edges(g, survey_response_list):
	""" Adds edges to labor graph

	Args:
		g: LaborGraph object
		survey_response_list: list that contains answers of the surverys
	"""
	for response in survey_response_list:
		# extract member name from survey
	    member = response['questions'][0]['answers'][0]['text']
	    g.add_edge('s', member, 4)
	    for answer in response['questions'][1]['answers']:
	        labor = LABOR_MAP[answer['row']][answer['col']]
	        if(labor != 0):
	            g.add_edge(member, labor, 2)

	for labor in LABORS_LIST:
	    g.add_edge(labor[0], 't', labor[1])

if __name__ == '__main__':
    main()