def transpose_matrix(arr,r,c):
    for i in range(0,r):
        for j in range(i+1,c):
            arr[i][j],arr[j][i] = arr[j][i],arr[i][j]
    return arr
    
arr = [[1,2,3],[4,5,6],[7,8,9]]
print(transpose_matrix(arr,3,3))
