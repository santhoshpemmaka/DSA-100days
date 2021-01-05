ef string_subnets(string,current,i):
    if i == len(string):
        print(current)
        return 
    else:
        # print(current)
        string_subnets(string,current,i+1)
        string_subnets(string,current+string[i],i+1)
        
string_subnets("abc","",0)
