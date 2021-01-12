def last_occurence(arr,x):
    first = 0
    last = len(arr)-1
    while first <= last:
        mid = (first+last)//2
        if arr[mid] > x:
            last = mid -1
        elif arr[mid] < x:
            first = mid+1
        if mid == len(arr)-1 or arr[mid] != arr[mid+1]:
            return mid
        else:
            first = mid+1
    return -1

arr = [5,5,5]
print(last_occurence(arr,5))

def last_occurence1(arr,x,first,last):
    if first > last:
        return -1
    mid = (first + last)//2
    if arr[mid] > x:
        return last_occurence1(arr,x,first,mid-1)
    elif arr[mid] < x:
        return last_occurence1(arr,x,mid+1,last)
    if mid == len(arr)-1 or arr[mid] != arr[mid+1]:
        return mid
    else:
        return last_occurence1(arr,x,mid+1,last)
    
print(last_occurence1(arr,5,0,len(arr)-1))
        
