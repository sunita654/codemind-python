n=int(input())
l=list(map(int,input().split(" ")))
k=list(map(int,input().split(" ")))
p=[]
for i in range(n):
    p.append(str(l[i]+k[i]))
print(" ".join(p))