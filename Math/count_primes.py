import math

class Solution(object):
    def countPrimes(self, number):
        
        if(number==0 or number==1):
            return 0;
        result = [True for i in range(0,number)]
        sqrt_number = int(math.sqrt(number))
        for i in range(2,sqrt_number+1):
            if result[i]:
                for j in range(2*i,number,i):
                    result[j] = False
                    
        count =0
        for i in range(2,number):
            if result[i]:
                count= count+1
        return count
