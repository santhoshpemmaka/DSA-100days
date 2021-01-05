def cutting_rod(rod_length,a,b,c):
    if rod_length == 0:
        return 0
    if rod_length < 0:
        return -1
        
    result = max(cutting_rod(rod_length-a,a,b,c),
                cutting_rod(rod_length-b,a,b,c),
                cutting_rod(rod_length-c,a,b,c))
    if result == -1:
        return -1
    else:
        return result+1
        
print(cutting_rod(23,11,9,12))
print(cutting_rod(5,2,5,1))
