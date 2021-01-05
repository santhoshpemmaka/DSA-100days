def factorial(num):
    if num==0 or num==1:
        return 1
    else:
        return num*factorial(num-1)
        
print(factorial(5))


def fibonacci_number(num):
    if num == 0:
        return 0
    if num ==1:
        return 1
    return fibonacci_number(num-1)+fibonacci_number(num-2)
print(fibonacci_number(3))
