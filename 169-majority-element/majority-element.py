class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count =1
        curr = nums[0]
        i =1
        while i<len(nums):
            if nums[i]==curr:
                count+=1
            else:
                count -=1
            if not count:
                curr= nums[i]
                count=1
            i+=1    
        return curr                

        