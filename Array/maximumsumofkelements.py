def maximumsumofkelements(arr,k):
    maximumsum = 0
    for i in range(len(arr)-k):
        sum1 =0
        for j in range(i,i+k):
            sum1 = sum1 + arr[j]
        maximumsum = max(maximumsum,sum1)
    return maximumsum
    
arr = [1,8,30,-5,20,7]
print(maximumsumofkelements(arr,3))

def maximumsumofelements1(arr,k):
    current_max = 0
    maximum = 0
    for i in range(0,k):
        current_max = current_max+arr[i]
    maximum= current_max
    for i in range(k,len(arr)):
        current_max += (arr[i] - arr[i-k] )
        maximum = max(current_max,maximum)
    return maximum
    
print(maximumsumofelements1(arr,3))

# Given the sum, if check sum present in subarray of the k elements

def checksumof_kelements(arr,k,sum1):
    current_max = 0
    for i in range(k):
        current_max = current_max+arr[i]
    if current_max == sum1:
        return 1
    for i in range(k,len(arr)):
        current_max += arr[i] - arr[i-k]
        if current_max == sum1:
            return 1
    return 0
    
print(checksumof_kelements(arr,3,41))
