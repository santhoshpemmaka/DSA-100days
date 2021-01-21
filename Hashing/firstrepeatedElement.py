def firstRepeated(arr, n):
    
    #arr : given array
    #n : size of the array
    min = -1
    result = {}
    for i in range(n-1,-1,-1):
        
        if arr[i] in result.keys():
            min = i
        else:
            result[arr[i]]= 1
            
    if min == -1:
        return -1
    else:
        return min+1
