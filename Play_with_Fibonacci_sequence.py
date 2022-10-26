a=0
b=1
n=int(input())
print(a,b,end=" ")
for i in range(2,n):
    c=a+b
    a=b
    b=c
    if(n!=n-1): print(c,end=" ")
    else:print(c)
    