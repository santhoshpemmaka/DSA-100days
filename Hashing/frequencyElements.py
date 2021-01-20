def frequencyElements(arr):
    list_frequency = {}
    for i in range(len(arr)):
        if arr[i] in list_frequency.keys():
            list_frequency[arr[i]] +=1
        else:
            list_frequency[arr[i]] = 1
    print(list_frequency)
    
    
arr = [10,12,10,15,10,20,12,12,13]
frequencyElements(arr)
