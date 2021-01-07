def maximumdifference(arr): # arr[j] - arr[i] such that j>i
    maximumdifference = arr[1] - arr[0]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if (arr[j] - arr[i]) > maximumdifference:
                maximumdifference = arr[j] - arr[i]
    return maximumdifference
    
arr = [2,3,10,6,4,8,1]
arr1 = [30,10,8,2]
print(maximumdifference(arr1)) # TIme Complexity = 0(n**2)

def maximumdifference1(arr):
    maximum = arr[1] - arr[0]
    minimum = arr[0]
    for i in range(1,len(arr)):
        maximum = max(maximum,arr[i]- minimum)
        minimum = min(minimum,arr[i])
    return maximum
    
arr = [2,3,10,6,4,8,1]
arr1 = [30,10,8,2]
print(maximumdifference1(arr)) # Time complexity = 0{n)
