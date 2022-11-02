n=int(input())
l=list(map(int,input().split(" ")))
k=0
for i in range(len(l)):
    k+=1
result=0
if(k==int(n)):
    for j in range(len(l)):
        for h in range(len(l)):
            if (h>j):
                if(int(l[h])!=0):
                    if(int(l[j])!=0):
                        if(int(l[j])==int(l[h])):
                               l[j]=0
                               l[h]=0
                               result +=1                     
    print(result)