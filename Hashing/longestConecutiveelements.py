def longestConsecutive(arr):
    count = 1
    res = 1
    arr.sort()
    for i in range(1,len(arr)):
        if arr[i-1]+1 == arr[i]:
            count = count+1
        else:
            res = max(res,count)
            count = 1
            
    return max(res,count)
    
    
def longestConsecutive1(arr):
    res = 0
    hash = set()
    for i in range(len(arr)):
        hash.add(arr[i])

    for i in range(len(arr)):
        if arr[i] - 1 not in hash:
            curr = 1
            while arr[i]+1 in hash:
                curr+=1
            res = max(curr,res)
            
    return res
        
        
arr = [1,9,3,4,2,20]
arr1 = [8,20,7,30]
print(longestConsecutive1(arr))
