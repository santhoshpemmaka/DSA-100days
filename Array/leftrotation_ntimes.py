def leftrotation(arr):
    temp = arr[0]
    res = 0
    for i in range(1,len(arr)):
        arr[res] = arr[i]
        res = res+1
    arr[len(arr)-1] = temp
    return arr
    
def leftrotation1(arr,d):
    for i in range(d):
        leftrotation(arr)
    print(arr)
    
arr = [1,2,3,4,5,6,7]
leftrotation1(arr,2) # TimeComplexity = 0(n*d)

def leftrotation_ntimes(arr,d):
    n = len(arr)
    temp = []
    for i in range(d):
        temp.append(arr[i])
    for i in range(d,len(arr)):
        arr[i-d] = arr[i]
    
    for i in range(len(temp)):
        arr[n-d-i] = temp[i]
        
arr1 = [1,2,3,4,5,6]
print(leftrotation_ntimes(arr,2)) # TimeComplexity = 0(n) spaceComplexity = 0(d)

def reverseorder(arr,low,high):
    while low< high:
        arr[low],arr[high] = arr[high],arr[low]
        low = low+1
        high = high-1
        
def leftrotation_ntimes1(arr,d):
    reverseorder(arr,0,d-1)
    reverseorder(arr,d,len(arr)-1)
    reverseorder(arr,0,len(arr)-1)
    return arr
arr2 = [1,2,3,4,5,6]
print(leftrotation_ntimes1(arr2,2)) # TimeComplexity = 0{n) spacecomplexity = 0(1)
