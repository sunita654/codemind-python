def inde(s):
    for i in range(len(s)):
        if s.count(s[i])==1:return i
    return -1
s=input()
p=inde(s)
print(p)