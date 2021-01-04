import math

def check_prime(number):
    if number<=1:
        return False
    if number == 2 or number==3:
        return True
    if number %2 ==0 or number%3 ==0:
        return False
        
    for i in range(5,int(math.sqrt(number)+1),6):
        if number % i ==0 or number%(i+2) ==0:
            return False
    return True

def print_primenumbers(number):
    for i in range(2,number+1):
        if check_prime(i):
            print(i)
            

def print_primenumbers1(number):
    result = [True for i in range(number+1)]
    for i in range(number+1):
        if i%2 ==0  or i%3 ==0 or i%5 ==0:
            result[i] = False
    for i in range(number+1):
        if result[i]:
            print(i)

print_primenumbers1(100)
print_primenumbers(13)
