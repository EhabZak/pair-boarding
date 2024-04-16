from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)
        for src, dst in redEdges:
            red[src].append(dst)
        for src, dst in blueEdges:
            blue[src].append(dst)
        print ( 'red *******', red)

        answer = [-1 for _ in range(n)]
        queue = deque ([(0,0,None)])
        visited = set ([(0 , None)])
        print ('queue', queue)

        while queue:
            print ('queue', queue)

            node, length ,edgeColor = queue.popleft()
            print('visited ^^^^^^', visited)
            print ('queueafter pop %%%%%%%%%%%%%%%%%%%%%%%%%%', queue)
            if answer[node] == -1:
                answer[node] = length
            if edgeColor != 'Red':
                for neighbor in red[node]:
                    print('neighbor =========',neighbor)
                    if (neighbor,'Red') not in visited:
                        visited.add((neighbor,'Red'))
                        queue.append((neighbor,length+1,'Red'))
            if edgeColor != 'Blue':
                for neighbor in blue[node]:
                    if (neighbor,'Blue') not in visited:
                        visited.add((neighbor,'Blue'))
                        queue.append((neighbor,length+1,'Blue'))
        return answer



n = 3
redEdges = [] #[0,1,-1]
redEdges = [[0,1],[1,2]] #[0,1,-1]
# blueEdges = [[0,1],[1,2]] #[0,1,-1]
blueEdges = []
sol = Solution()
print(sol.shortestAlternatingPaths(n,redEdges,blueEdges))
