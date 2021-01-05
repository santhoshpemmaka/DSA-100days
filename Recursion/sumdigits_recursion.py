def sumdigits_recursion(num):
    if num==0:
        return 0
    else:
        return num%10+sumdigits_recursion(num//10)

print(sumdigits_recursion(982))
