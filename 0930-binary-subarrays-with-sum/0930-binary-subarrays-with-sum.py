class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        p={0:1}
        s=0
        a=0
        m=len(nums)
        for i in range(m):
            s=s+nums[i]
            if s-goal in p:
                a+=p[s-goal]
            p[s]=p.get(s,0)+1
        return a
                
        