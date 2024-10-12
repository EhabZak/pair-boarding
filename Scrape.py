from typing import List
from typing import Optional, List
from collections import defaultdict, Counter

#! List (b): [0.3434, 0.1234, 0.565, 0.665, 0.656]
#!######################################
def insertionSort(b):
    for i in range(1,len(b)):
        # print ("========b is: ==>", b)
        up = b[i]  #! up = 0.1234
        j = i-1 #! 0
        while j >= 0 and b[j] > up:  #! b[j] = 0.3434
            b[j+1] =b[j] # i.e j+1 = 1 and b[j+1] = 0.3434
            j -= 1 # j = j-1 => j = -1 exit the while loop since j < 0
            b[j+1] = up # b[0] = 0.1234
    return b

