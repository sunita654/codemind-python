def countOddSum(ar, n):
    result = 0
    for i in range(n):
        val = 0
        for j in range(i, n ):
            val = val + ar[j]
            if (val % 2 != 0):
                result +=1
 
    return (result)
arr = []
p=int(input())
n=int(input())
for i in range(p,n+1):arr.append(i)
print(countOddSum(arr, len(arr)))