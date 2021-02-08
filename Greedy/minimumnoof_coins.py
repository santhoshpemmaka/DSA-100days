import math

def minimum_coins(arr,amount):
    arr.sort(reverse = True)
    res = 0
    for i in range(len(arr)):
        if arr[i] <= amount:
            c = math.floor(amount//arr[i])
            res = res + c
            amount = amount - (c*arr[i])
        if amount == 0:
            break
    return res
        
    

arr = [1,5,2,10]
print(minimum_coins(arr,57))
