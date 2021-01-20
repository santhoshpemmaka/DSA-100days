
def intersectionElements(arr,arr1):
    count = 0
    for i in range(len(arr)):
        flag = False
        for j in range(len(arr1)):
            if arr[i] == arr1[j]:
                flag = True
                break
        if flag == True:
            count = count+1
    return count
    
def intersectionElements1(arr,arr1):
    arr = set(arr)
    arr1 = set(arr1)
    print(arr,arr1)
    count = 0
    for i in arr:
        if i in arr1:
            count = count+1
    return count



arr = [10,15,20,15,30,30,5]
arr1 = [30,5,30,80]
arr2 = [10,10]
arr3 = [10,10]
print(intersectionElements1(arr2,arr3))
