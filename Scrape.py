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
#! x = [0.897, 0.565, 0.656,0.1234, 0.665, 0.3434]
######################################
def bucketSort(x):
    arr = []
    slot_num = 10 # Number of buckets
    # create the buckers
    for i in range(slot_num):
        arr.append([])
        print('arr is' ,arr)

    # Put array elements into different buckets
    for j in x:
        # print( '==jj=', j)
        index_b = int(slot_num*j) # Index of the bucket
        # print ("index b ==>", index_b)
        arr[index_b].append(j)
        # print(arr)

    # Sort individual buckets using insertion sort
    for i in range(slot_num):
        # print ('arr[i]', arr[i])
        arr[i]= insertionSort(arr[i])

    # Concatenate sorted buckets into the original array
    k = 0
    for i in range (slot_num):
        # print ('slotNumber', slot_num)
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k +=1
    return x

x = [0.897, 0.565, 0.656,
	0.1234, 0.665, 0.3434]

print("Sorted Array is")
print(bucketSort(x))


# def insertionSort2(bb):
#     for i in range (1, len(bb)):
#         up = bb[i]
#         j = i-1
#         while j >= 0 and bb[j]> up:
#             bb[j+1] = bb[j]
#             j = j-1
#             bb[j+1]= up
#     return bb



# b2= [0.3434, 0.1234, 0.565, 0.665, 0.656]
# print(insertionSort2(b2))
