def b(s):
        l,c=0,0
        for i in s:
            if i=='L':
                l+=1
            else:
                l-=1
            if l==0:
                c+=1
        return c
s=input()
print(b(s))