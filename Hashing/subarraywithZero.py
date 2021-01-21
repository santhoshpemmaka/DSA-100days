def givensubarraySumzero(arr):
    for i in range(len(arr)):
        curry_sum = 0
        for j in range(i,len(arr)):
            curry_sum += arr[j]
            if curry_sum == 0:
                return True
    return False
    
    
def givensubarraySumzero1(arr):
    result = set()
    prefix_sum = 0
    for i in range(len(arr)):
        prefix_sum +=arr[i]
        if prefix_sum in result:
            return "Yes"
        if prefix_sum == 0:
            return "Yes"
        result.add(prefix_sum)
    return "No"
    
arr = [1,4,-13,-3,16,5]
print(givensubarraySumzero1(arr))
