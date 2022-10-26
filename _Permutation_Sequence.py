class Solution:
    def P(self, n: int, k: int) -> str:
        from itertools import permutations
        nm=[i for i in range(1,n+1)]
        p=list(permutations(nm))
        return "".join(str(i) for i in p[k-1])
ob=Solution()
n,k=map(int,input().split(" "))
print(ob.P(n,k))