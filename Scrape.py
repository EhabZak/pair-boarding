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
######################################
def bucketSort(x):
    arr = []
    slot_num = 10 # Number of buckets
    for i in range(slot_num):
        arr.append([])
        # print(arr)

    # Put array elements into different buckets
    for j in x:
        print( '==jj=', j)
        index_b = int(slot_num*j) # Index of the bucket
        arr[index_b].append(j)
        print(arr)

    # Sort individual buckets using insertion sort
    for i in range(slot_num):
        arr[i]= insertionSort(arr[i])

    # Concatenate sorted buckets into the original array
    k = 0
    for i in range (slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k +=1
    return x


