def movingzerosend(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] !=0:
            arr[count] = arr[i]
            count = count+1
    while count<len(arr):
        arr[count] = 0
        count = count+1
    
def movingzerosend1(arr):
    count = 0
    for i in range(0,len(arr)):
        if arr[i] != 0:
            arr[count],arr[i] = arr[i],arr[count]
            count= count+1
    return arr

arr = [8,5,10,0,20,0]
movingzerosend1(arr)
print(arr)
