l=int(input())
r=int(input())
n=l
while(n<=r):
   count=0
   for i in range(1,n+1):
       if(n%i==0):
            count+=1
   if(count==2):
      print(n)
   n+=1