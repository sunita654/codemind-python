n=int(input())
l=list(map(int,input().split(" ")))
p=[]
for i in l:
    p.append(i*i)
p.sort()
k=[]
for i in p:
    k.append(str(i))
print(" ".join(k))