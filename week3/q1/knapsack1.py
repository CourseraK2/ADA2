'''
    
    In this programming problem and the next you'll code up the knapsack algorithm from lecture. Let's start with a warm-up. Download the text file here[http://spark-public.s3.amazonaws.com/algo2/datasets/knapsack1.txt]. This file describes a knapsack instance, and it has the following format:
    [knapsack_size][number_of_items]
    [value_1] [weight_1]
    [value_2] [weight_2]
    ...
    For example, the third line of the file is "50074 659", indicating that the second item has value 50074 and size 659, respectively.
    
    You can assume that all numbers are positive. You should assume that item weights and the knapsack capacity are integers.
    
    In the box below, type in the value of the optimal solution.
    
    ADVICE: If you're not getting the correct answer, try debugging your algorithm using some small test cases. And then post them to the discussion forum!
'''
# Programming Assignment #2
# knapsack problem
# https://class.coursera.org/algo2-002/quiz/attempt?quiz_id=85
# Question 1
def build_items(file_name):
	new_file = open(file_name, 'r')
	WEIGHT, n = [int(x) for x in new_file.readline().split()]

	items = [[int(x) for x in new_file.readline().split()] for i in range(n)]

	return WEIGHT, items

def knapsack(weight, items):
	# initialization
	n = len(items)
	DP = {} # memoization
	for w in xrange(weight+1):
		DP[(-1, w)] = 0

	for i in xrange(n):
		for w in xrange(weight+1):
			vi, wi = items[i][0], items[i][1]
			if wi > w:
				DP[(i, w)] = DP[(i-1, w)]
			else:
				DP[(i, w)] = max(DP[(i-1, w)], DP[(i-1, w-wi)] + vi)

		for w in xrange(weight+1):
			DP.pop((i-1, w))


	return DP[(n-1, weight)]
def main():
	WEIGHT, items = build_items('knapsack1.txt')
	res = knapsack(WEIGHT, items)
	print res

if __name__ == '__main__':
	main()
			
