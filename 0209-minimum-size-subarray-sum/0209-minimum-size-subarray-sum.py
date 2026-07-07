class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        s=0
        m=float('inf')
        n=len(nums)
        for j in range(n):
            s+=nums[j]
            while s>=target:
                m=min(m,j-i+1)
                s-=nums[i]
                i+=1
        return m if m!=float('inf') else 0


            

            
                