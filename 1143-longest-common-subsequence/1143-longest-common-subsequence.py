class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # def fun(i,j):
        #     if i<0 or j<0:
        #         return  0
        #     if text1[i]==text2[j]:
        #         return 1+fun(i-1,j-1)
        #     return max(fun(i-1,j),fun(i,j-1))
        # return fun(len(text1)-1,len(text2)-1)
        dp=[[0]*(len(text2)+1) for i in range(len(text1)+1)] 
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]                                       