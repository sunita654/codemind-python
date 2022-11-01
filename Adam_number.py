n=input()
k=str(int(n)*int(n))
p=n[::-1]
m=str(int(p)*int(p))
if(m==k[::-1]):
    print("True")
else:
    print("False")