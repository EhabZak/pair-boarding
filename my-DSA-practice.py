from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
       nodeColors = {}
       print ('nodeColors', nodeColors) #{}

##########################################################################
       def colorNodes(node, currentColor): # recursive function
           print ('node ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^', node)
           if node in nodeColors: # Check if the node is already colored
               print ('node in nodeColors #####',node)
               print ('nodeColors[node] == currentColor =>$$$$$$$$$$',nodeColors[node] == currentColor)
               print (f'nodeColors[node]=, {nodeColors[node]} , currentColor is = {currentColor}')

               return nodeColors[node] == currentColor # Check if the color matches
           nodeColors[node] = currentColor # if node not in nodeColors then Color the current node with the given color
           print ('nodeColors after nodeColors[node] = currentColor!!!!!!', nodeColors)
           print ('nodeColors[node]==== ', nodeColors[node] )
           print('currentColor *****', currentColor  )

           for neighbor in graph[node]: #! second iteration through the node and neighboring nodes
               if not colorNodes(neighbor,not currentColor): # if colorNodes returns false it will be not False (True) then this condition will apply
               # if not (True) it means this condition is false thus not applicable
                   return False
           return True
##########################################################################
       #! execution start
       for node in range(len(graph)): #! first iteration through all the nodes
           print ('===========================================>>>>>>>>>>>>>>>>>>START AGAIN')
           #Checks if the node is not already colored and colors it with True (considering it as part of set A).
           print('colorNodes(node,True)@@@@@@@@@@@@@@@@@@@@@@@',colorNodes(node,True))
           if node not in nodeColors and not colorNodes(node,True): #! why does it have to be true and red is not working?
               return False
       print ('nodeColors at the end', nodeColors)
       return True


# graph = [[1,2,3],[0,2],[0,1,3],[0,2]] # False
graph = [[1,3],[0,2],[1,3],[0,2]] #True
# graph = [[1,3],[0,2],[1,3],[0,2],[4,5,6]] #True , this is working fine
# graph = [[1,3],[0,2],[1,3],[0,2],[5,6]] #! not working why?

#
sol = Solution()
print(sol.isBipartite(graph))
