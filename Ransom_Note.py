class Solution:
    def c(self, s1: str, s2: str) -> bool:
        d = {}
        for i in s2:
            if i in d:
                d[i] +=1
            else:
                d[i] = 1
        for i in s1:
            if i not in d:
                return False
            else:
                d[i] -=1
                if d[i] == 0:
                    d.pop(i)
        return True
s1,s2=map(str,input().split(" "))
ob=Solution()
print(ob.c(s1,s2))