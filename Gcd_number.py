## GCD of the number of the navie approach.

def gcd_number(num,num1):
    result = min(num,num1)
    while(result>0):
        if num%result ==0 and num1%result == 0:
            break;
        result = result-1
    return result
    
print(gcd_number(2,4))
 
## Time complexitity = 0(min(num,num1))

## GCD of the number using Eucliclean algorithm.

def gcd(num,num1):
    if(num1 == 0):
        return num
    else:
        return gcd(num1,num%num1)

print(gcd(7,10))
