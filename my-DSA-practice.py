from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
       target = len(graph)-1
       results= []

       def backtrack( currentNode, path):
           if currentNode == target:
               results.append(list(path))
               return
           for neighbor in graph[currentNode]:
               path.append(neighbor)
               backtrack(neighbor,path)
               path.pop()
       path = [0]
       backtrack(0,path)


       return results



graph = [[1,2],[3],[3],[]]

sol = Solution()
print(sol.allPathsSourceTarget(graph))
