def stack_buy_sell(arr):
    profit = 0
    for i in range(1,len(arr)):
        if arr[i] > arr[i-1]:
            profit +=arr[i]-arr[i-1]
    return profit
    
arr = [10,20,30]
print(stack_buy_sell(arr))
