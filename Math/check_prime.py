import math

def check_prime(number):
    if number <=1:
        return False
    if number == 2:
        return True
    for i in range(2,number):
        if number%i ==0:
            return False
    return True
    
def check_prime1(number):
    if(number<=1):
        return False
    if number ==2:
        return True
    for i in range(2,int(math.sqrt(number))+1):
        if number % i==0:
            return False
    return True
    
def check_prime2(number):
    if(number<=1):
        return False
    if(number==2 or number==3):
        return True
    if(number%2 ==0 or number%3 ==0):
        return False
    for i in range(5,number,6):
        if number%i ==0 or number%(i+2) ==0: # check with ith number and i+2th number
            return False
    return True

print(check_prime2(29))
