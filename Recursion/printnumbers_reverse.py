def print_number(num):
    if num==0:
        return 
    print(num)
    return print_number(num-1)
    
print_number(5)
