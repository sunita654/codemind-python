def isPronicNumber(num):    
    flag = "NO"   
    for j in range(1, num+1):    
        if((j*(j+1)) == num):    
            flag = "YES"  
            break    
    return flag  
n=int(input())
print(isPronicNumber(n))