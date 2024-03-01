class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)
        prev = 1
        for i in range(1,len(nums)):
            prev *=nums[i-1]
            result[i]=prev
        bp = 1    
        for i in range(len(nums)-2,-1,-1):
            bp*= nums[i+1]
            result[i]=result[i]*bp
        return result    

        