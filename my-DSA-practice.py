from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


#! 43- 785. Is Graph Bipartite? (Medium) (algo: adjacency list , dfs)  (time complexity ???))

'''
785. Is Graph Bipartite?
Medium
Topics
Companies TikTok Apple Amazon
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.



Example 1:


Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.

'''

#! with full explanation

# class Solution:
#     def isBipartite(self, graph: List[List[int]]) -> bool:
#        nodeColors = {}
#        print ('nodeColors', nodeColors) #{}

# ##########################################################################
#        def colorNodes(node, currentColor): # recursive function
#            print ('node ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^', node)
#            if node in nodeColors: # Check if the node is already colored
#                print ('node in nodeColors #####',node)
#                print ('nodeColors[node] == currentColor =>$$$$$$$$$$',nodeColors[node] == currentColor)
#                print (f'nodeColors[node]=, {nodeColors[node]} , currentColor is = {currentColor}')

#                return nodeColors[node] == currentColor # Check if the color matches
#            nodeColors[node] = currentColor # if node not in nodeColors then Color the current node with the given color
#            print ('nodeColors after nodeColors[node] = currentColor!!!!!!', nodeColors)
#            print ('nodeColors[node]==== ', nodeColors[node] )
#            print('currentColor *****', currentColor  )

#            for neighbor in graph[node]: #! second iteration through the node and neighboring nodes
#                if not colorNodes(neighbor,not currentColor): # if colorNodes returns false it will be not False (True) then this condition will apply
#                # if not (True) it means this condition is false thus not applicable
#                    return False
#            return True
# ##########################################################################
#        #! execution start
#        for node in range(len(graph)): #! first iteration through all the nodes
#            print ('===========================================>>>>>>>>>>>>>>>>>>START AGAIN')
#            #Checks if the node is not already colored and colors it with True (considering it as part of set A).
#            print(f'loop == {node}')
#            if node not in nodeColors and not colorNodes(node,True): #! why does it have to be true and red is not working?
#                return False
#        print ('nodeColors at the end', nodeColors)
#        return  True


# graph = [[1,2,3],[0,2],[0,1,3],[0,2]] # False
# # graph = [[1,3],[0,2],[1,3],[0,2]] #True
# sol = Solution()
# print(sol.isBipartite(graph))





# class Solution:
#     def fib(self, n: int, memo ={}) -> int: # this is depth first search

#         # if n == 0 : return 0
#         # if n == 1 : return 1
#         # if n in memo: return memo[n]

#         # memo[n]= self.fib(n-1,memo)+ self.fib(n-2, memo)
#         # return memo[n]
#


# #! Fastest solution
# class Solution:
#     def fib(self, n: int, mono = {}) -> int:
#         if n==0: return 0
#         elif n==1 or n==2: return 1

#         else:
#             x=[0,1]
#             o=2
#             while o<n:
#                 x.append(x[o-1]+x[o-2])
#                 o=o+1

#             # print('X at the end == ',x)
#             return x[n-1]+x[n-2]



# n = 10
# solution = Solution()
# output = solution.fib(n)
# print(output)






def fib_tab(n):

    if n < 2: return n

    dp = [0,1]
    i = 2

    while i <= n:
        tmp = dp[1]
        dp[1] = dp[0]+ dp[1]
        dp[0]= tmp
        i +=1
    return dp[1]





n = 10

print(fib_tab(n))
