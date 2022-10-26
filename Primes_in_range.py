def seive(m):
    p=[1 for i in range(m+1)]
    p[0]=0
    p[1]=0
    i=2
    while (i*i<=m):
        if p[i]==1:
            for j in range(i*i,m+1,i):
                p[j]=0
        i+=1
    return p
n=int(input())
m=int(input())
l=seive(m)
c=0
for i in range(n,m+1):
    if(l[i]):
        c+=1
print(c)