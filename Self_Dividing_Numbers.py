n=int(input())
m=int(input())
for i in range(n,m+1):
    i=str(i)
    c=0
    for j in i:
        if(j!="0" and int(i)%int(j)==0):c+=1
    if(c==len(i)):print(i,end=" ")