def InsertionSort(arr):
    for i in range(1, len(arr)):
        j = i-1
        while j>= 0 and arr[j]>arr[i]:
            arr[j+1] = arr[i]
            j = j-1
            arr[j+1] = arr[i]
        
