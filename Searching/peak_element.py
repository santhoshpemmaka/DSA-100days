def peak_element(arr):
    low =0 
    high = len(arr)-1
    n = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if (mid==0 or arr[mid-1]<arr[mid]) and (mid==n or arr[mid]> arr[mid+1]):
            return arr[mid]
        elif mid >0 and arr[mid-1] > arr[mid]:
            high = mid-1
        else:
            first = mid+1
    return -1
    
arr = [5,10,20,15,7]
print(peak_element(arr))
