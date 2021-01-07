def even_odd_subarray(arr):
    result = 1
    for i in range(0,len(arr)):
        current =1
        for j in range(i+1,len(arr)):
            if(arr[j] % 2 == 0 and arr[j-1] % 2 != 0) or (arr[j] % 2 !=0 and arr[j-1]%2 ==0 ):
                current = current+1
            else:
                break
        result = max(result,current)
    return result
    
arr = [1,3,2,5,4]
print(even_odd_subarray(arr)) # Time Complexity = 0(n**2)

def even_odd_subarray1(arr):
    result = 1
    current = 1
    for j in range(1,len(arr)):
        if(arr[j] % 2 == 0 and arr[j-1] % 2 != 0) or (arr[j] % 2 !=0 and arr[j-1]%2 ==0 ):
            current = current+1
            result = max(result,current)
        else:
            
            current = 1
    return result
    
arr = [1,3,2,5,4]
print(even_odd_subarray1(arr))
            
