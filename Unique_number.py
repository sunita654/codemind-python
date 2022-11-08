def unique(n):
    for i in n:
        if n.count(i)>1:return "Not Unique Number"
    return "Unique Number"
n=input()
print(unique(n))