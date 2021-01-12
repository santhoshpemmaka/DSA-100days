def countones_sorted(arr):
    first = 0
    last = len(arr)-1
    while first <= last:
        mid = (first+last)//2
        if arr[mid] == 0:
            first = mid+1
        else:
            if mid ==0 or arr[mid] != arr[mid-1]:
                return len(arr)-mid
            else:
                last = mid-1
    return 0
    
arr = [0,0,0,0,1,1,1]
print(countones_sorted(arr))
