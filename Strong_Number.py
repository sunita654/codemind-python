n=int(input())
k=[]
for i in str(n):
    s=1
    for j in range(2,int(i)+1):
        s*=j
    k.append(s)
if(sum(k)==n):
    print("The number {} is a strong number".format(n))
else:
    print("The number {} is not a strong number".format(n))