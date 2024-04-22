from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
       # itirate thought graph
       # create a dfs function check if the node in color node check if the color is correct
       # if node not in color node then we assign a color to it
       # we visit its neighbors and assing a color opposite to node
       nodeColor = {}
       def dfs(node,currentColor):
           if node in nodeColor:
               return nodeColor[node] == currentColor
           nodeColor[node]= currentColor

           for neighbor in graph[node]:
               if not dfs(neighbor, not currentColor):
                   return False
           return True




       for node in range(len(graph)):
           if node not in nodeColor and not dfs(node, True):
               return False
       return True






# graph = [[1,2,3],[0,2],[0,1,3],[0,2]] # False
graph = [[1,3],[0,2],[1,3],[0,2]] #True
sol = Solution()
print(sol.isBipartite(graph))
