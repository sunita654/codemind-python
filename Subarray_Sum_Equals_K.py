n,k=map(int,input().split())
arr=list(map(int,input().split()))
m=len(arr)
res=0
for i in range(m):
    sum=0
    for j in range(i,m):
        sum=sum+arr[j]
        if(sum==k):
           res+=1
print(res)
        
