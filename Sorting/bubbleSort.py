def bubbleSort(arr):
    for i in range(0,len(arr)):
        flag = False
        for j in range(1,len(arr)-i):
            if arr[j-1] > arr[j]:
                arr[j],arr[j-1] = arr[j-1],arr[j]
                flag = True
        if flag == False:
            break
    return arr
    
arr = [12,4,5,6,7,9,10,-12]
arr1 = [6,7,8,9,10]
print(bubbleSort(arr1))
