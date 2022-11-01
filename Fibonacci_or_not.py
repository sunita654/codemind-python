def fibonacci(n):
    a=0
    b=1
    if(n==0 and n==1):
        return True
    for i in range(n-1):
        c=a+b
        a,b=b,c
        if(c==n):
            return True
    return False
n=int(input())
print(fibonacci(n))
    