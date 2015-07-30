'''
    In this assignment you will implement one or more algorithms for the traveling salesman problem, such as the dynamic programming algorithm covered in the video lectures. Here is a data file describing a TSP instance[http://spark-public.s3.amazonaws.com/algo2/datasets/tsp.txt]. The first line indicates the number of cities. Each city is a point in the plane, and each subsequent line indicates the x- and y-coordinates of a single city.
    
    The distance between two cities is defined as the Euclidean distance --- that is, two cities at locations (x,y) and (z,w) have distance sqrt((x−z)^2+(y−w)^2) between them.
    
    In the box below, type in the minimum cost of a traveling salesman tour for this instance, rounded down to the nearest integer.
    
    OPTIONAL: If you want bigger data sets to play with, check out the TSP instances from around the world here[http://www.tsp.gatech.edu/world/countries.html]. The smallest data set (Western Sahara) has 29 cities, and most of the data sets are much bigger than that. What's the largest of these data sets that you're able to solve --- using dynamic programming or, if you like, a completely different method?
    
    HINT: You might experiment with ways to reduce the data set size. For example, trying plotting the points. Can you infer any structure of the optimal solution? Can you use that structure to speed up your algorithm?
'''
# Programming Assignment #4
# https://class.coursera.org/algo2-002/quiz/attempt?quiz_id=93
# this algorithm is not practical, it is too slow.
import math
import sys
import itertools

infinity = sys.maxint

def euclidean_distance(point1, point2):
	return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# def buildAdjList(file_name):
# 	""" file -> list of dictionary

# 	Return a list of list of lists, which represent a undirect graph.

# 	the index of the list is the number of the vertex
# 	and the value of the according index is the adjacent vertex

# 	example: 
# 			[{2: 100, 3: 1000}, {6: 10000, 7: 100000}] -> the 0 vertex has edges to 2, 3 vertex,
# 											 and the weight is 100 and 1000 respectively
# 										   the 1 vertex has edges to 6, 7 vertex, and the weith is 10000
# 										   and 100000 respectively.

# 	"""
# 	input_file = open(file_name, 'r')
# 	city_n = int(input_file.readline().strip())
# 	cities = []
# 	for line in input_file:
# 		x, y = [float(x) for x in line.strip().split()]
# 		cities.append((x, y))
	
# 	adjList = []	
# 	for v in xrange(city_n):
# 		inner_dic = {}
# 		for v2 in xrange(city_n):
# 			if v != v2:
# 				distance = euclidean_distance(cities[v], cities[v2])
# 				inner_dic[v2] = distance

# 		adjList.append(inner_dic)

# 	return city_n, adjList

# ## unit test
# # def main():
# # 	graph = buildAdjList('tsp.txt')
# # 	print graph
# ## unit test

# def tsp_brute_force(n, graph):
# 	length = infinity

# 	start_node = 0
# 	other_nodes = range(1, n)
# 	# use itertools.permutations to get all the possible path
# 	# which need O(n!) time
# 	all_path = itertools.permutations(other_nodes)
# 	count = 0
# 	for path in all_path:
# 		print 'count->', count
# 		count += 1

# 		length_path = 0
# 		current_node = start_node

# 		for next_node in path:
# 			length_path += graph[current_node][next_node]
# 			current_node = next_node

# 		length_path += graph[current_node][start_node]

# 		if length_path < length:
# 			length = length_path

# 	return length

	

# def main():
# 	n, graph = buildAdjList('tsp.txt')
# 	print tsp_brute_force(n, graph)

# if __name__ == '__main__':
# 	main()