class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp=[[False]*(len(p)+1) for i in range(len(s)+1)]
        dp[0][0]=True
        for i in range(1,len(p)+1):
            if p[i-1]=='*':
                dp[0][i]=dp[0][i-1]
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if s[i-1]==p[j-1] or p[j-1]=='?':
                    dp[i][j]=dp[i-1][j-1]
                if p[j-1]=='*':
                    dp[i][j]=dp[i][j-1]
                    if j-2 >=0 and s[i-1]==p[j-2] or p[j-1]=='?':
                        dp[i][j]=dp[i][j] or dp[i-1][j]
                    elif j-1>=0:
                        dp[i][j]=dp[i][j] or dp[i-1][j]
        return dp[-1][-1]

















        # def fun(i,j):
        #     if i<0 and j<0:
        #         return True
        #     if i==-1 or j==-1:
        #         return False
        #     if p=="*":
        #         return True
        #     if s[i]!=p[j]:
        #         if s[i]=="*":
        #             return(fun(i,j-1) or fun(i-1,j))
        #         if s[i]=="?":
        #             return fun(i-1,j-1)
        #         else:
        #             return False
        #     else:
        #         return fun(i-1,j-1) 
        # return fun(len(s)-1,len(p)-1)