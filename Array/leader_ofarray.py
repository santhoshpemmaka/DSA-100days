def leaderof_array(arr):
    for i in range(len(arr)):
        flag = False
        for j in range(i+1,len(arr)):
            if arr[i] <= arr[j]:
                flag = True
                break
        if flag == False:
            print(arr[i],end=" ")
            
arr = [7,10,4,10,6,5,2]
print(leaderof_array(arr))

# naive approach Time complexity = 0(n**2)
# Space complexity = 0(1)

def leaderof_array1(arr):
    l1 = []
    last_index = len(arr)-1
    current_leader = arr[last_index]
    l1.append(current_leader)
    for i in range(last_index-1,-1,-1):
        if current_leader < arr[i]:
            current_leader = arr[i]
            l1.append(current_leader)
    print(l1[::-1])        
    
arr = [7,10,4,10,6,5,2]
print(leaderof_array1(arr))

# better approach Timw Complexity = 0(n)
# space Complexity = 0(n)
    
