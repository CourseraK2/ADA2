'''
    In this assignment you will implement one or more algorithms for the 2SAT problem. Here are 6 different 2SAT instances: #1[https://spark-public.s3.amazonaws.com/algo2/datasets/2sat1.txt] #2 #3 #4 #5 #6.
    
    The file format is as follows. In each instance, the number of variables and the number of clauses is the same, and this number is specified on the first line of the file. Each subsequent line specifies a clause via its two literals, with a number denoting the variable and a "-" sign denoting logical "not". For example, the second line of the first data file is "-16808 75250", which indicates the clause .
    
    Your task is to determine which of the 6 instances are satisfiable, and which are unsatisfiable. In the box below, enter a 6-bit string, where the ith bit should be 1 if the ith instance is satisfiable, and 0 otherwise. For example, if you think that the first 3 instances are satisfiable and the last 3 are not, then you should enter the string 111000 in the box below.
    
    DISCUSSION: This assignment is deliberately open-ended, and you can implement whichever 2SAT algorithm you want. For example, 2SAT reduces to computing the strongly connected components of a suitable graph (with two vertices per variable and two directed edges per clause, you should think through the details). This might be an especially attractive option for those of you who coded up an SCC algorithm for Part I of this course. Alternatively, you can use Papadimitriou's randomized local search algorithm. (The algorithm from lecture might be too slow, so you might want to make one or more simple modifications to it to ensure that it runs in a reasonable amount of time.) A third approach is via backtracking. In lecture we mentioned this approach only in passing; see the DPV book[http://www.cs.berkeley.edu/~vazirani/algorithms/chap9.pdf], for example, for more details.
'''
import math
import random
import gc
import sys
import threading
from StringIO import StringIO

def make_sat_graph(clauses):
    n = len(clauses)
    def var_index(var):
        if var < 0: return n - var
        else: return var
    res = []
    for clause in clauses:
        res.append( '%i %i\n' % (var_index(-clause[0]), var_index(clause[1])))
        res.append( '%i %i\n' % (var_index(-clause[1]), var_index(clause[0])))
        # print 'res', res
    return res
        
        
################################################################################
#######      Kosaraju's SSC algorithm implementation from part 1          ######
################################################################################

def readDirectedGraph(str):
    # f = StringIO(str)
    # print 'str->', str
    
    adjlist = []
    adjlist_reversed = []
    
    # line = f.readline()
    # print "line->", line
    # while line != '':
    for line in str:
        num1, num2 = line.split()
        v_from = int(num1)
        v_to = int(num2)
        max_v = max(v_from, v_to)
        
        while len(adjlist) < max_v:
            adjlist.append([])
        while len(adjlist_reversed) < max_v:
            adjlist_reversed.append([])
            
        adjlist[v_from-1].append(v_to-1)
        adjlist_reversed[v_to-1].append(v_from-1)
        
        # line = f.readline()
            
    return adjlist, adjlist_reversed


t = 0
s = None
n = 0
explored = None
leader = None
current_ssc = None
contradictory_ssc = None
sorted_by_finish_time = None

def DFS_Loop_1(graph_rev, n):
    
    global t, explored, sorted_by_finish_time
    
    t = 0
    explored = [False]*n
    sorted_by_finish_time = [None]*n
    
    for i in reversed(range(n)):
        if not explored[i]:
            DFS_1(graph_rev, i)
                        
            
def DFS_1(graph_rev, i):
    
    global t, explored
    
    explored[i] = True
    
    for v in graph_rev[i]:
        if not explored[v]:
            DFS_1(graph_rev, v)
    
    sorted_by_finish_time[t] = i
    t += 1
    
    
def DFS_Loop_2(graph):
    
    global current_ssc, explored, contradictory_ssc, sorted_by_finish_time
    
    explored = [False]*len(graph)
    
    for i in reversed(range(len(graph))):
        if not explored[sorted_by_finish_time[i]]:
            scc_size = 0
            # Here we collect all the members
            # of the next SCC using DFS.
            current_ssc = set()
            contradictory_ssc = False
            DFS_2(graph, sorted_by_finish_time[i])
            if contradictory_ssc: break
            
    return contradictory_ssc
    
    
def DFS_2(graph, i):
    
    global explored, current_ssc, contradictory_ssc
    
    explored[i] = True
    current_ssc.add(i)
    
    # Check for unsatisfabilty indicator
    if i < n:
        if (i+n) in current_ssc:
            contradictory_ssc = True
    elif (i-n) in current_ssc:
        contradictory_ssc = True
    
    for v in graph[i]:
        if not explored[v]:
            DFS_2(graph, v)
    

def kosaraju_contradictory_ssc(graph, graph_rev):
    
    DFS_Loop_1(graph_rev, len(graph))
    contradictory_ssc = DFS_Loop_2(graph)
    
    return contradictory_ssc


def main():

    global n

    for i in xrange(1, 7):
        print 'file %i' % i
        f = open('2sat%i.txt' % i)
        n = int(f.readline())
        clauses = [[int(x) for x in line.split()] for line in f]
        
        sat_graph = make_sat_graph(clauses)
        graph, graph_rev = readDirectedGraph(sat_graph)
        contradictory_ssc = kosaraju_contradictory_ssc(graph, graph_rev)
        res = 'unsatisfiable' if contradictory_ssc else 'satisfiable'
        
        print 'result: %s\n' % res
        
        gc.collect()


if __name__ == '__main__':
    threading.stack_size(67108864) # 64MB stack
    sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
    thread = threading.Thread(target = main) # instantiate thread object
    thread.start() # run program at target