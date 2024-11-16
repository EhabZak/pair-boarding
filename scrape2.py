
def insertionSort(arr):
    for i in range(1,len(arr)):
        j = i-1
        while j >= 0 and arr[j]> arr[i]:
            # arr[j+1] = arr[j]
            # j = j -1
            # arr[j+1]= arr[i]
        # ele = arr[i]
        # while j >= 0 and arr[j]> ele:
        #     arr[i] = arr[j]
        #     arr[j] = ele
            arr[i] ,[j] = arr[j], [i]
            j-=1
    return arr

x = [0.897, 0.565, 0.656,0.1234, 0.665, 0.3434]
print (insertionSort(x))

# def bucketSort(x):
#     array = []
#     slot_num = 10
#     for i in range (slot_num):
#         array.append([])

#     for j in x:
#         index_b = int(slot_num*j)
#         array[index_b].append(j)

#     for i in range(slot_num):
#         array[i]= insertionSort(array[i])

#     k = 0
#     for i in range (slot_num):
#         for j in range (len(array[i])):
#             x[k]= array[i][j]
#             k +=1
#     return x



# x = [0.897, 0.565, 0.656,
# 	0.1234, 0.665, 0.3434]

# print("Sorted Array is")
# print(bucketSort(x))

'''
/*
Comparison Sorting
Quicksort usually has a running time of n x log(n) , but is there an
algorithm that can sort even faster? In general, this is not possible.
Most sorting algorithms are comparison sorts, i.e. they sort a list
just by comparing the elements to one another. A comparison sort
algorithm cannot beat  (worst-case) running time, since  represents
the minimum number of comparisons needed to know where to place each
element. For more details, you can see these notes (PDF).

Alternative Sorting
Another sorting method, the counting sort, does not require comparison. Instead, you create an integer array whose index range covers the entire range of values in your array to sort. Each time a value occurs in the original array, you increment the counter at that index. At the end, run through your counting array, printing the value of each non-zero valued index that number of times.

Example


