
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
