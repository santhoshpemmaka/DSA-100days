def trappingwater(arr):
    result = 0
    lmax=[]
    lmax.append(arr[0])
    for i in range(1,len(arr)):
        left_max = max(lmax[i-1],arr[i])
        lmax.append(left_max)
    print(lmax)
    rmax = [0 for i in range(len(arr)-1)]
    rmax.insert(len(arr)-1,arr[len(arr)-1])
    for i in range(len(arr)-2,-1,-1):
        right_max = max(rmax[i+1],arr[i])
        rmax[i] = right_max
    print(rmax)
    for i in range(1,len(arr)-1):
        result = result+ (min(lmax[i],rmax[i]) - arr[i])
    return result
    
arr = [5,0,6,2,3]
print(trappingwater(arr))
