def maximum_consecutive1s(arr):
    result1 = -1
    result = 0
    
    for i in range(len(arr)):
        if arr[i] ==1:
            result = result+1
        elif result1 == -1 or result > result1:
            result1 = result
            result =0
    
    return max(result,result1)
    
arr = [0,0,1,1,1,0,0,0,1,1,1,1]
arr1 = [1,1,1,1]
arr2 = [0,0,0,1]
print(maximum_consecutive1s(arr))
