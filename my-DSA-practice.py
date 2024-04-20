from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
       colorNodes= {}

       def colorTheNodes(node,currentColor):
           if node in colorNodes:
               return colorNodes[node] == currentColor
           colorNodes[node] = currentColor

           for neighbor in graph[node]:
               if not colorTheNodes(neighbor, not currentColor):
                   return False
           return True


       for node in range(len(graph)):
           if node not in colorNodes and not colorTheNodes(node,True):
               return False
       return True







graph = [[1,2,3],[0,2],[0,1,3],[0,2]] # False
# graph = [[1,3],[0,2],[1,3],[0,2]] #True
# graph = [[1,3],[0,2],[1,3],[0,2],[4,5,6]] #True , this is working fine
# graph = [[1,3],[0,2],[1,3],[0,2],[5,6]] #! not working why?

#
sol = Solution()
print(sol.isBipartite(graph))
