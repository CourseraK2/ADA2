'''
    This problem also asks you to solve a knapsack instance, but a much bigger one.
    
    Download the text file here[http://spark-public.s3.amazonaws.com/algo2/datasets/knapsack_big.txt]. This file describes a knapsack instance, and it has the following format:
    [knapsack_size][number_of_items]
    [value_1] [weight_1]
    [value_2] [weight_2]
    ...
    For example, the third line of the file is "50074 834558", indicating that the second item has value 50074 and size 834558, respectively. As before, you should assume that item weights and the knapsack capacity are integers.
    
    This instance is so big that the straightforward iterative implemetation uses an infeasible amount of time and space. So you will have to be creative to compute an optimal solution. One idea is to go back to a recursive implementation, solving subproblems --- and, of course, caching the results to avoid redundant work --- only on an "as needed" basis. Also, be sure to think about appropriate data structures for storing and looking up solutions to subproblems.
    
    In the box below, type in the value of the optimal solution.
    
    ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then post them to the discussion forum!
'''
# Programming Assignment #2
# knapsack problem
# https://class.coursera.org/algo2-002/quiz/attempt?quiz_id=85
# Question 2
import sys
sys.setrecursionlimit(10000)

def build_items(file_name):
	new_file = open(file_name, 'r')
	WEIGHT, n = [int(x) for x in new_file.readline().split()]

	items = [[int(x) for x in new_file.readline().split()] for i in range(n)]

	return WEIGHT, items

def knapsack_top_down(weight, items): # use recursive
	n = len(items)
	print 'n-> ', n
	DP = {} # memoization
	def knapsack_dic(i, w):
		if (i, w) in DP:
			return DP[(i, w)]
		if i == 0:
			return 0
		else:
			vi, wi = items[i][0], items[i][1]
			if wi > w:
				res = knapsack_dic(i-1, w)
				DP[(i, w)] = res

			else:
				res = max(knapsack_dic(i-1, w), knapsack_dic(i-1, w-wi) + vi)
				DP[(i, w)] = res

			return res
	return knapsack_dic(n-1, weight)

def main():
	WEIGHT, items = build_items('knapsack_big.txt')
	res = knapsack_top_down(WEIGHT, items)
	print res

if __name__ == '__main__':
	main()
			
