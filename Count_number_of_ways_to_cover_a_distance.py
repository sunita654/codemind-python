def isdist(n):
    if n<0:
        return 0
    if n==0:
        return 1
    
    return (isdist(n-1) +
            isdist(n-2) +
            isdist(n-3))
 
        
n=int(input())
print(isdist(n))
