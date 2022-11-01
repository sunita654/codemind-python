n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
k=int(input())
c=0
for i in l:
    if(i<=k):c+=1
    else:c+=2
print(c)