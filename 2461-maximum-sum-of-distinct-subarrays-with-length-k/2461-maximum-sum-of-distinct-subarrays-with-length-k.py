class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        m=0
        i=0
        d={}
        s=0
        for j in range(n):
            d[nums[j]]=d.get(nums[j],0)+1
            s+=nums[j]
            if j-i+1==k:
                if len(d)==k:
                    m=max(m,s)
                d[nums[i]]-=1
                if d[nums[i]]==0:
                    del d[nums[i]]
                s-=nums[i]
                i+=1
        return m




        