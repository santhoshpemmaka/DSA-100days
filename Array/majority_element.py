def majority_element(arr):
    n = len(arr)
    for i in range(len(arr)):
        count = 1
        for j in range(i+1,len(arr)):
            if arr[j] == arr[i]:
                count = count+1
        if count > n//2:
            return i
    return -1
    
arr = [8,2,8,6,8,7,7]
print(majority_element(arr)) #Time complexity = 0(n**2)

def majority_element1(arr):
    count =1 
    res = 0
    for i in range(1,len(arr)):
        if arr[i] == arr[res]:
            count = count+1
        else:
            count = count-1
        if count == 0:
            res = i
            count =1
    count1 = 0
    print(res)
    for i in range(len(arr)):
        if arr[res] == arr[i]:
            count1 = count1+1
    if count1 <= len(arr)//2:
        return -1
    else:
        return res
        
arr = [8,2,8,6,8,8,8]
print(majority_element1(arr))

