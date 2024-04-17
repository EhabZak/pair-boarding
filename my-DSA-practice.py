from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        redDict = defaultdict(list)
        blueDict = defaultdict(list)

        for src, dst in redEdges:
            redDict[src].append(dst)
        for src, dst in blueEdges:
            blueDict[src].append(dst)


        answer = [- 1 for _ in range(n)]
        queue = deque([(0,0,None)]) # node length ,prev color
        visited = set([(0, None)])

        while queue:
            node, length ,prevColor = queue.popleft()
            if answer[node] == -1:
                answer[node] = length

            if prevColor != 'Red':
                for neighbor in redDict[node]:
                    if (neighbor,'Red') not in visited:
                        visited.add((neighbor,'Red'))
                        queue.append((neighbor,length+1, 'Red'))
            if prevColor != 'Blue':
                for neighbor in blueDict[node]:
                    if (neighbor,'Blue') not in visited:
                        visited.add((neighbor,'Blue'))
                        queue.append((neighbor,length+1,'Blue'))
        return answer



n = 3
# redEdges = [[0,1],[1,2]] #[0,1,-1]
# blueEdges = []
#Ex2
# redEdges = []
# blueEdges = [[0,1],[1,2]] #[0,1,-1]
#ex3
# redEdges = [[0,1]]
# blueEdges = [[2,1]] #[0,1,-1]
#ex4
redEdges = [[0,1]]
blueEdges = [[1,2]] #[0,1,2]
sol = Solution()
print(sol.shortestAlternatingPaths(n,redEdges,blueEdges))
