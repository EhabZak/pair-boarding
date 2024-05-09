from typing import List
from typing import Optional, List
from collections import defaultdict, Counter,deque
import heapq
import math, random

#! 1- Remove Zeros (AA)

'''
take out the zeros and add them at the end of the list
'''
# num = [0, 1, 0, 3, 12]

# def numZero(num) :
#     count = 0

#     i = 0
#     while i < len(num):
#         n = num[i]
#         if n == 0 :
#             # num.remove(n)
#             # del num[i]
#             num.pop(i)
#             count +=1

#         else:
#             i +=1
#     # num.extend([0]* count)
#     # or you can use
#     for _ in range (count):
#         num.append(0)



# numZero(num)
# print (num) # [ 1, 3, 12, 0, 0 ]


num = [0, 1, 0, 3, 12]

def numZero(num):
    pass

numZero(num)
print (num) # [ 1, 3, 12, 0, 0 ]
