def large(l, n, m):
    for i in range(m):
        p= l[0][i]
        for j in range(n):
            if l[j][i] > p:
                p = l[j][i]
        print(p)
n, m = map(int,input().split(" "))
l=[]
for i in range(n):
    k=list(map(int,input().split(" ")))
    l.append(k)
large(l, n, m);