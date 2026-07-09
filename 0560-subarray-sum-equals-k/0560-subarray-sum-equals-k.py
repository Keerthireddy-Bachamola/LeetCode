class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        p={0:1}
        s=0
        a=0
        m=len(nums)
        for i in range(m):
            s=s+nums[i]
            if s-k in p:
                a=a+p[s-k]
            p[s]=p.get(s,0)+1
        return a  