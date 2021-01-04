def compute_power(number,number1):
    result =1
    for i in range(number1):
        result = result*number
    return result
    
def compute_power1(number,number1):
    if number1 == 0:
        return 1
    temp = compute_power1(number,number1//2)
    temp = temp*temp
    if(number1 %2 ==0):
        return temp
    else:
        return temp*number
    
print(compute_power1(2,3))
