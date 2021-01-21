def subarraywithgivensum(arr,sum1):
    for i in range(len(arr)):
        subarray_sum = 0
        for j in range(i,len(arr)):
            subarray_sum += arr[j]
            if subarray_sum == sum1:
                return True
    return False
    
def subarraywithgivensum1(arr,sum1):
    result = set()
    prefix_sum = 0
    for i in range(len(arr)):
        prefix_sum += arr[i]
        if prefix_sum == sum1:
            return True
        if prefix_sum-sum1 in result:
            return True
        result.add(prefix_sum)
    return False
    
arr = [5,8,6,13,4,-1]
sum1 = 20
print(subarraywithgivensum1(arr,sum1))

