def palindrone_string(str1,start,end):
    if start>=end:
        return True
    if str1[start] == str1[end]:
        return palindrone_string(str1,start+1,end-1)
    else:
        return False
        
print(palindrone_string("abddba",0,len("abddba")-1))
