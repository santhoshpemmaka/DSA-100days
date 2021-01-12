def first_occurence(arr,x):
    first = 0
    last = len(arr)-1
    while first <= last:
        mid = (first+last)//2
        if arr[mid] > x:
            last = mid -1
        elif arr[mid] < x:
            low = mid+1
        if arr[mid] != arr[mid-1] or mid ==0:
            return mid
        else:
            last = mid -1
    return -1
            
arr =[5,5,5]
print(first_occurence(arr,5))

def first_occurence1(arr,x,first,last):
    if first > last:
        return -1
    mid = (first+last)//2
    if arr[mid] > x:
        return first_occurence1(arr,x,first,mid-1)
    elif arr[mid] < x:
        return first_occurence1(arr,x,mid+1,last)
    if arr[mid] != arr[mid-1] or mid==0:
        return mid
    else:
        return first_occurence1(arr,x,first,mid-1)
        
print(first_occurence1(arr,5,0,len(arr)-1))
    
