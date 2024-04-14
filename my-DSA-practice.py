from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


# class Solution:
#     def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
#        target = len(graph)-1
#        result = []

#        def backtrack(currentNode,path):
#            if currentNode == target:
#                result.append(path.copy())

#            for number in graph[currentNode]:
#                path.append(number)
#                backtrack(number,path)
#                path.pop()




#        path = [0]
#        backtrack(0,path)


#        return result



# graph = [[1,2],[3],[3],[]]

# sol = Solution()
# print(sol.allPathsSourceTarget(graph))




class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph)-1
        result = []

        def backtrack(currentNode,path):
            if currentNode == target:
                result.append(path.copy())
                return

            for number in graph[currentNode]:
                path.append(number)
                backtrack(number,path)
                path.pop()

        path = [0]
        backtrack(0,path)

        return result

graph = [[1,2],[3],[3],[]]

sol = Solution()
print(sol.allPathsSourceTarget(graph))
