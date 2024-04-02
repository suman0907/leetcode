class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        l = 0
        r =0
        res =0
        while r<len(nums):
            jump =0
            for i in range(l,r+1,1):
                jump = max(jump,i+nums[i])
            if jump>=len(nums)-1:
                break    
            l = r+1
            r = jump
            res +=1 
        return res+1       
             
        