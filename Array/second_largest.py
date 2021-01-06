# navie approach solution

def secondlargest(arr):
    result = arr[0]
    for i in range(1,len(arr)):
        if arr[i]> result:
            result = arr[i]
    result1 = arr[1]
    for i in range(2,len(arr)):
        if arr[i] > result1 and result != arr[i]:
            result1 = arr[i]
    if result == result1:
        print(-1)
    return result1
    
secondlargest([10,10,10])


# Better apporach 

def secondlargest1(arr):
    result = arr[0]
    result1 = -1
    for i in range(1,len(arr)):
        if arr[i] > result:
            result1 = result
            result = arr[i]
        elif arr[i] != result:
            if result1 == -1 or arr[i] > result1:
                result1 = arr[i]
    return result1
    
print(secondlargest1([12,7,12,9]))
    
