class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele = nums[0]
        count = 1
        i = 1
        while i<len(nums):
            if nums[i]==ele:
                count +=1
            else:
                count -=1
            if count==0:
                ele = nums[i]
                count =1
            i+=1
        return ele            

        