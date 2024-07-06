from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random


class Solution(object):
    def lengthOfLongestSubstring(self, s):
       window = set()
       left,right =  0
       max_l = 0

       while right < len(s):
           while s[right] in window:
               window.discard(s[left])
               left +=1
               max_l = max(max_l, right-left+1)
               window.add(s[right])
               right +=1
               return max_l

'''
in this question we used a while loop in the 2nd loop and not if
 because The while loop continues to execute as long as the condition s[right] in window is true
 The if statement is executed only once per outer loop iteration.
'''

s = "abcabcbb"
solution = Solution()
output = solution.lengthOfLongestSubstring(s)
print(output)
