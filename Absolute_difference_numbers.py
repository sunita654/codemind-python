n,m=map(int,input().split(" "))
n=str(n)
p=int(n[:m:])
k=""
for i in range(len(n)-m,len(n)):
    k+=n[i]
k=int(k)
print(abs(p-k))