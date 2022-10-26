class Solution:
    def increasingNumbers(self, N):
        #code here
        ans = []
        if N==0:
            return ans
        else:
            if N == 1:
                ans.append(0)
            def add_digit(s, last):
                if len(s) == N:
                    ans.append(int(s))
                else:
                    for digit in range(last+1, 11-N+len(s)):
                        add_digit(s+str(digit),digit)
            add_digit("",0)
            return ans

N = int(input())
ob = Solution()
ans = ob.increasingNumbers(N)
for num in ans:
        print(num,end=' ')