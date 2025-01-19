
def insertionSort(arr):
    for i in range(1,len(arr)):
        j = i-1
        print(arr[j])
        while j >= 0 and arr[j]> arr[i]:
            arr[j+1] = arr[j]
            j = j -1
            arr[j+1]= arr[i]
        # ele = arr[i]
        # while j >= 0 and arr[j]> ele:
        #     arr[i] = arr[j]
        #     arr[j] = ele
        #     arr[i] ,[j] = arr[j], [i]
        #     j-=1
    return arr


