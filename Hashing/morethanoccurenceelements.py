def morethanoccurence(arr,k):
    for i in range(len(arr)):
        count = 1
        for j in range(i+1,len(arr)):
            if arr[i] == arr[j]:
                count = count+1
        if count > len(arr)//k:
            print(arr[i],end=" ")
            
            
def morethanoccurence1(arr,k):
    result = {}
    for i in range(len(arr)):
        if arr[i] in result:
            result[arr[i]] +=1
        else:
            result[arr[i]] = 1
    print(result)
    for i in result:
        if result[i] > len(arr)//k:
            print(i,end=" ")
arr = [30,10,20,20,10,20,30,30]
morethanoccurence1(arr,4)
