def pushZerosToEnd(arr, n):
    count = 0 
    for i in range(n):
        if arr[i] != 0:
            arr[count] = str(arr[i])
            count+=1
    while count < n:
        arr[count] = "0"
        count += 1
         
n = int(input())
arr =list(map(int,input().split(" ")))
pushZerosToEnd(arr, n)
print(" ".join(arr))