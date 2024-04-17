from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
       nodeColors = {}
       Len = len(graph)

       def colorNodes(node, currentColor):
           if node in nodeColors:
               return nodeColors[node] == currentColor
           nodeColors[node] = currentColor

           for neighbor in graph[node]:
               if not colorNodes(neighbor,not currentColor):
                   return False
           return True
       for node in range(Len):
           if node not in nodeColors and not colorNodes(node,True):
               return False
       return True







# graph = [[1,2,3],[0,2],[0,1,3],[0,2]] # False
graph = [[1,3],[0,2],[1,3],[0,2]] #True
sol = Solution()
print(sol.isBipartite(graph))
