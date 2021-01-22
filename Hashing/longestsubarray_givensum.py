def longestsubarray_sum(arr,sum1):
    result = {}
    prefix_sum = 0
    longest_subarray = 0
    for i in range(len(arr)):
        prefix_sum +=arr[i]
        if prefix_sum == sum1:
            longest_subarray = i+1
        if prefix_sum not in result:
            result[prefix_sum] = i
        if prefix_sum - sum1 in result:
            longest_subarray = max(longest_subarray,i-result[prefix_sum-sum1])
    print(result)
    print(longest_subarray)
    
arr = [5,8,-4,-4,9,-2,2]
arr1 = [8,3,7]

longestsubarray_sum(arr1,14)
