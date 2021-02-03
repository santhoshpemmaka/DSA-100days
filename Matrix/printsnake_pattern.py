def pattern_snakePattern(arr):
    for i in range(len(arr)):
        if i%2 == 0:
            for j in range(len(arr[i])):
                print(arr[i][j],end=" ")
        else:
            for j in range(len(arr[i])-1,-1,-1):
                print(arr[i][j],end=" ")
    print()
        
arr = [[1,2,3],[4,5,6],[7,8,9]]
pattern_snakePattern(arr)
