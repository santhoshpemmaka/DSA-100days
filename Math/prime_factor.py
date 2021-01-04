## prime factor of the given number
import math

def check_prime(number):
    if number <=1:
        return False
    if number ==2 or number ==3:
        return True
    if number% 2 ==0 or number%3 ==0:
        return False
    for i in range(5,int(math.sqrt(number))+1,6):
        if number% i ==0 or number% (i+2) == 0:
            return False
    return True
    
def prime_factors(number):
    for i in range(2,number):
        if(check_prime(i)):
            x = i
            while (number%x ==0):
                print(i)
                x= x*i
                
                
## Efficicent apporach

def prime_factors1(number):
    if number<=1:
        return False
    for i in range(2,int(math.sqrt(number))+1):
        while number% i==0:
            print(i)
            number = number//i
    if number>1:
        print(number)
prime_factors1(450)
            
prime_factors(15)
