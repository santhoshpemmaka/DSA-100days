def selectionSort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index],arr[i] = arr[i],arr[min_index]
    return arr
            
arr = [12,4,5,6,7,9,10,-12]
arr1 = [6,7,8,9,10]
print(selectionSort(arr))
