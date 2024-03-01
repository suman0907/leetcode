class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = 0
        r = 0
        while r<len(nums)-1:
            jump = 0
            for i in range(l,r+1,1):
                jump = max(jump,i+nums[i])
            l = r+1
            r = jump
            res +=1
        return res        
        