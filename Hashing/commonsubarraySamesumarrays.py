def commonsumof_arrays(arr,arr1):
    longest_subarray = 0
    for i in range(len(arr)):
        sum1 = 0
        sum2 = 0
        for j in range(i,len(arr)):
            sum1 +=arr[j]
            sum2 +=arr1[j]
            if sum1 == sum2:
                longest_subarray = max(longest_subarray,j-i+1)
    return longest_subarray
    
def commonsumof_arrays1(arr,arr1):
    longest_subarray = 0
    temp = [0 for i in range(len(arr))]
    for i in range(len(arr)):
        temp[i] = arr[i] - arr1[i]
    result = dict()
    prefix_sum = 0
    for i in range(len(temp)):
        prefix_sum += arr[i]
        if prefix_sum not in result:
            result[prefix_sum] = i
        if prefix_sum - 0 in result:
            longest_subarray = max(longest_subarray,i-result[prefix_sum-0])
    return longest_subarray
        
    
arr = [0,1,0,0,0,0]
arr1 = [1,0,1,0,0,1]
print(commonsumof_arrays1(arr,arr1))
