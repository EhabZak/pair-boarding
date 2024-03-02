from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pts= []

        for x, y in points:
            dist = math.sqrt(abs(x-0)**2 + abs(y-0)**2)
            pts.append([dist,x , y] )

        res = []
        heapq.heapify(pts)
        # print(pts)

        for i in range(k):
            dist, x , y = heapq.heappop(pts)
            res.append([x,y])

        return res




# points = [[1,3],[-2,2]]
# k = 1


points = [[3,3],[5,-1],[-2,4]] # [[3,3],[-2,4]]
k = 2

sol = Solution()
print(sol.kClosest(points, k))
