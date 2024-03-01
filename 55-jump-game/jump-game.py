class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True    
        jump = 0
        target = len(nums)-1
        for i in range(len(nums)):
            jump = max(jump,i+nums[i])
            if jump<=i:
                return False
            if jump>= target:
                return True
        return False        

        