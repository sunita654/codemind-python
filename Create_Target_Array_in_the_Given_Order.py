n=int(input())
l=list(map(int,input().split(" ")))
k=int(input())
h=list(map(int,input().split(" ")))
p=[]
for i in range(len(l)):
    p.insert(h[i],str(l[i]))
print(" ".join(p))