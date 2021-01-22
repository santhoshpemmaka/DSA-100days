def windowsizedistictelement(arr,k):
    for i in range(k-1,len(arr)):
        result = set()
        for j in range(i,i-k,-1):
            result.add(arr[j])
        print(result)
        print(len(result),end=" ")
    
arr = [10,20,20,10,30,40,10]
k = 2
arr1 = [10,10,10,10,10,10]
windowsizedistictelement(arr1,k)
