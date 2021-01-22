# longest subarray with having equal 0's and 1's

def longestsubarray(arr):
    res = 0
    for i in range(len(arr)):
        c0=0
        c1=0
        for j in range(i,len(arr)):
            if arr[j] == 1:
                c1 = c1 + 1
            else:
                c0 = c0 + 1
        if c0 == c1:
            res = max(res,j-i+1)
    return res
    
def longestsubarray1(arr):
    longest_subarray = 0
    result = {}
    prefix_sum = 0
    for i in range(len(arr)): # replace all 0's with 1's in the array.
        if arr[i] == 0:
            arr[i] = -1
    for i in range(len(arr)):
        prefix_sum += arr[i]
        print(prefix_sum)
        if prefix_sum not in result:
            result[prefix_sum] = i
        if prefix_sum - 0 in result:
            longest_subarray = max(longest_subarray,i-result[prefix_sum - 0])
        # print(result)
    print(result)
    return longest_subarray

arr = [1,0,1,1,1,0,0]
print(longestsubarray1(arr))
