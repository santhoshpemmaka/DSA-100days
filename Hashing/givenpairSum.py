def givenpairSum(arr,sum1):
    result = set()
    for i in range(0,len(arr)):
        print(sum1-arr[i])
        if sum1-arr[i] in result:
            return "Yes"
        result.add(arr[i])
    return "No"

arr = [11,6,5]
sum1 = 10
print(givenpairSum(arr,sum1))


def givenpairsum(arr,sum1):
    result = set()
    for i in range(len(arr)):
        if sum1-arr[i] in result:
            return "Yes"
        result.add(arr[i])
    return "No"



arr = [2,3,5,7,8]
sum1 =11
print(givenpairsum(arr,sum1))
