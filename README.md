# Automatic Labor Assignment
This is a personal project to automate the labor assignment for Halstead Co-op.

Halstead is a housing co-op in which college students control the organization. Since the house is run by the own the students, there is something called labor. Labor is the share of the work necessary to operate the house, such as cooking, cleaning,  doing dishes, etc. This typically requires 4 hours per week by each person at the house. 

Labor schedules are manually assigned according to the student's aviability, so my goal is to automate this process. Members of the house fills out a short survey about their unavailibity. Here is the link of the survey:

https://www.surveymonkey.com/r/Y8Z7YTF

After getting all the members schedule, I run my python script to automatic assign labor according to their preferences.
My python script automatic assigns and prints the required labor to Halstead members based on their availability, which are collected through responses of the surveys. 

The algorithm is a modified version of Ford-Fulkerson's algorithm. First, the script creates a labor bipartite graph with two disjoint sets: Halstead members and Halstead labors. Then, a source vertex is added, which has an edge with every single Halstead member. Similarly, a sink vertex is added, which has an edge with every single Halstead labors. Then, the modified version of Ford-Fulkerson's algorithm is run. The labor assignment will be the edges that has a flow of one, ignoring the edges of the source and sink vertices.


