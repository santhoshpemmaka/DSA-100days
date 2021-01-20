def distinctElements(arr):
    res = 0
    for i in range(len(arr)):
        flag = False
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                flag = True
        if flag == False:
            res = res+1
    return res
    
def distinctElements1(arr):
    hash = set()
    for i in range(len(arr)):
        hash.add(arr[i])
    print(len(hash))
                
arr = [15,12,13,12,13,13,18]
print(distinctElements(arr))
distinctElements1(arr)
