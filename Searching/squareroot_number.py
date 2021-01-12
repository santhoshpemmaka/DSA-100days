def squareroot_number(num):
    low = 0
    high = num
    ans =-1
    while low <= high:
        mid = (low+high)//2
        if mid*mid == num:
            return mid
        elif mid*mid < num:
            low = mid+1
            ans = mid
        else:
            high = mid-1
    return ans
    
print(squareroot_number(17))
