from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


ad_max = [
  # these columns represent the relationship
   #0 1 2 3 4 5          # print ad-max[n]
   [0,1,1,1,0,0],#0    # 0 line 2 times  # 5 line 5 times # this line represents the node 0
   [1,0,0,0,1,1],#1    # 1 line 5 times  # 3 line 6 times
   [1,0,0,0,0,1],#2    # 4 line 6 time   # 0 line 2 times
   [1,0,0,0,0,0],#3    # 2 line 1  time
   [0,1,0,0,0,0],#4    # 5 line 3  time
   [0,1,1,0,0,0] #5    # 2 line 6  time
]

visited = [0,0,0,0,0,0]

def dfs(node):
    if visited[node] != 0:
        return
    else:
        visited[node]= 1
        num = 0
        for relation in ad_max[node]:
            if relation != 0:
                dfs(num)
            num +=1
        print (node)




print (dfs(0))
