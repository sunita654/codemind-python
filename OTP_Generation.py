s=input()
k=""
for i in s:
    if int(i)%2!=0:k+=str(int(i)*int(i))
print(k)