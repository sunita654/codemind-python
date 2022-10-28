import math
n=int(input())
left=2**(math.floor(math.log2(n)))
right=left*2
print(min(n-left,right-n))