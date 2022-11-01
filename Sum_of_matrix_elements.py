n=int(input())
m=int(input())
l=[]
for i in range(n):
    k=list(map(int,input().split(" ")))
    l.append(sum(k))
print(sum(l))