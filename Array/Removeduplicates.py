def removeduplicates(arr):
    l1 = []
    l1.append(arr[0])
    res = 1
    for i in range(1,len(arr)):
        if l1[res-1] != arr[i]:
            l1.append(arr[i])
            res = res+1
    return l1
    
print(removeduplicates([10,20,20,30,30,30]))


def removeduplicates1(arr):
    res = 1
    for i in range(1,len(arr)):
        if arr[res-1] != arr[i]:
            arr[res] = arr[i]
            res = res+1
    return res
    
    
print(removeduplicates1([10,20,20,30,30,30]))
