class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_s=nums[0]
        max_s=nums[0]
        for i in range(1,len(nums)):
            curr_s=max(nums[i],curr_s+nums[i])
            max_s=max(max_s,curr_s)
        return max_s
                
        