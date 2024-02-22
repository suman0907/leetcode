class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, curr = 1, nums[0]
        i=1
        while i<len(nums):
            if curr==nums[i]:
                count +=1
            else:
                count -=1
            if not count:
                curr= nums[i]
                count=1
            i+=1    
        return curr                
        