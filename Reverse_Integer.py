n=input()
l=[]
k=""
for i in n:
    l.append(i)
if(n[0]=="-"):
    k="-"
    l.remove("-")
if(n[len(n)-1]=="0"):
    l.remove("0")
l.reverse()
print(k+"".join(l))