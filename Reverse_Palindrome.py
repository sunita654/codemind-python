n=input()
x=int(n)
while(1):
  x+=int(str(x)[::-1])
  if(str(x)==str(x)[::-1]):break
print(x)