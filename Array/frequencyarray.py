def frequencyarray(arr):
    obj = {}
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count = count+1
        obj[arr[i]] = count
    for i in obj:
        print(i,obj[i])
    print(obj)
    
arr = [10,10,20,30,30,40]
print(frequencyarray(arr))
