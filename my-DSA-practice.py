from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random



class Solution(object):
    def calPoints(self, operations):
        num = []


        for o in operations:
            print(num)
            if o == '+':
                num.append((num[-1])+ num[-2])
            elif o == "D":
                num.append(num[-1] *2)
            elif o =='C':
                num.pop()
            else:
                num.append(int(o))

        total_sum = sum(num)

        return total_sum






# ops = ["5","2","C","D","+"] #30
ops = ["5","-2","4","C","D","9","+","+"] #27
solution = Solution()
output = solution.calPoints(ops)
print(output)
