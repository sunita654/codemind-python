n=int(input())
k=str(n*n)
c=0
for i in k:
    c+=int(i)
if(c==n):print("Neon Number")
else:print("Not Neon Number")