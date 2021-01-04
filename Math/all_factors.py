import math

def allfactors_number(number):
    for i in range(1,int(math.sqrt(number)+1)):
        if number%i ==0:
            print(i)
            if(i != number//i):
                print(number//i)

# all factors of the sort order

def allfactors_number1(number):
    for i in range(1,int(math.sqrt(number)+1)):
        if number%i ==0:
            print(i)
    for i in range(int(math.sqrt(number)+1),0,-1):
        if number%i ==0:
            print(number//i)
            
allfactors_number1(500)
