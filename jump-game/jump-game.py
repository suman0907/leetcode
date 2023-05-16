class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums[0]==0 and len(nums)>1:
            return False
        jump = 0
        target = len(nums)-1
        for i in range(len(nums)):
            if jump<i:
                return False
            j = i+nums[i]
            jump = max(j,jump)
            
            if j>=target:
                return True
        return False            
        