#### Trailing Zero's of the given number.

def Trailing_zero(number):
    count =0
    i =5
    while number//i >0:
        count = count+number//i
        i = i*5
    return count;
    
print(Trailing_zero(100))

## Time complexitiy = log(n)
