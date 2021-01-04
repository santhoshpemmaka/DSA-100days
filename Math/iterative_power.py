def binary_power(x,number):
    result =1
    while number>0:
        if(number%2 !=0):
            result = result * x
        x = x*x
        number = number//2
    return result
    
print(binary_power(2,5))
        
