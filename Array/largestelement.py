def largest_element(arr):
    result = arr[0]
    for i in range(1,len(arr)):
        if result < arr[i]:
            result = arr[i]
    return result
    
print(largest_element([10,5,20,8]))

# Time Complexity = 0(n)
