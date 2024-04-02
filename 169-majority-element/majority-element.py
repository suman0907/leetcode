class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = nums[0]
        count = 0
        i=0
        while i<len(nums):
            if nums[i]==result:
                count +=1
            else:
                count -=1
            if not count:
                result = nums[i] 
                count +=1  
            i+=1     
        return result        
        
        