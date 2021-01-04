# lcm of the number in navie approach
def lcm_number(num,num1):
    result = max(num,num1)
    while True:
        if result%num == 0 and result%num1 == 0:
            return result
        result = result+1
    # return result    
    
# lcm of the number in better approach
def gcd(num,num1):
    if num1 ==0:
        return num
    else:
        return gcd(num1,num%num1)
    
def lcm(num,num1):
    return num*num1 // gcd(num,num1)
    


print(lcm_number(2,7))
print(lcm(2,7))
