
def unionofArray(arr,arr1):
    arr = set(arr)
    for i in arr1:
        arr.add(i)
    return len(arr)

arr = [15,20,5,15]
arr1 = [15,15,15,20,10]
arr2 =[3,3,3]
arr3 =[3]
print(unionofArray(arr2,arr3))
