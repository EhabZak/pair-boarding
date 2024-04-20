from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random





# graph = [[1,2,3],[0,2],[0,1,3],[0,2]] # False
graph = [[1,3],[0,2],[1,3],[0,2]] #True
# graph = [[1,3],[0,2],[1,3],[0,2],[4,5,6]] #True , this is working fine
# graph = [[1,3],[0,2],[1,3],[0,2],[5,6]] #! not working why?

#
sol = Solution()
print(sol.isBipartite(graph))
