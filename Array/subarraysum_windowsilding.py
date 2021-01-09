def subarraysum(arr,sum1):
    for i in range(len(arr)):
        current_sum = 0
        for j in range(i,len(arr)):
            current_sum += arr[j]
            if sum1 == current_sum:
                return 1
    return 0
    
arr = [1,4,20,3,10,5]
print(subarraysum(arr,33)) # Time Complexity = 0(n**2)

def subarraysum1(arr,sum1):
    s = 0
    e = 0
    current_sum = arr[0]
    for e in range(1,len(arr)):
        while current_sum > sum1 and s < e-1:
            current_sum -= arr[s]
            s = s+1
        if current_sum == sum1:
            return 1
        if current_sum < sum1:
            current_sum += arr[e]
    if current_sum == sum1:
        return 1
    else:
        return 0
        
print(subarraysum1(arr,31))
            
