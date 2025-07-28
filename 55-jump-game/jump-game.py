class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        if nums[0]==0:
            return False

        target = len(nums)-1
        jump = 0
        for i in range(0,len(nums)-1):
            jump=max(jump,i+nums[i])
            if jump<=i:
                return False
            if jump>=target:
                return True
        return False            
        