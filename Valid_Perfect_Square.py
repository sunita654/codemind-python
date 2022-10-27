import math
n=int(input())
for i in range(n):
    k=int(input())
    root=math.sqrt(k)
    if(int(root+0.5) ** 2==k):
        print("True")
    else:
        print("False")