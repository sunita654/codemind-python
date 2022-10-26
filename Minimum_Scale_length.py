def fgcd(x, y):
    while(y):
        x, y = y, x % y
    return x
p=int(input())
l=list(map(int,input().split(" ")))  
n1=l[0]
n2=l[1]
gcd=fgcd(n1,n2)
for i in range(2,len(l)):
    gcd=fgcd(gcd,l[i])
print(gcd)