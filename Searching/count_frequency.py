def first_occurence(arr,x):
    first = 0
    last = len(arr)-1
    while first <= last:
        mid = (first+last)//2
        if arr[mid] > x:
            last = mid -1
        elif arr[mid] < x:
            first = mid+1
        else:
            if mid==0 or arr[mid] != arr[mid-1]:
                return mid
            else:
                last = mid-1
    return -1

def last_occurence(arr,x):
    first = 0
    last = len(arr)-1
    while first <= last:
        mid = (first+last)//2
        print("last",mid)
        if arr[mid] > x:
            last = mid -1
        elif arr[mid] < x:
            first = mid+1
        else:
            if mid==len(arr)-1 or arr[mid] != arr[mid+1]:
                return mid
            else:
                first = mid+1
    return -1

    
def count_occurence(arr,x):
    first = first_occurence(arr,x)
    if first == -1:
        return 0
    return (last_occurence(arr,x)-first+1)

    
arr = [10,20,20,20,40,40]
print(count_occurence(arr,30))
      
