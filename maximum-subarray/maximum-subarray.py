class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        gsum = nums[0]
        curr_sum =nums[0]
        for i in range(1,len(nums)):
            curr_sum = max(curr_sum+nums[i],nums[i])
            gsum = max(curr_sum,gsum)
        return gsum    
        