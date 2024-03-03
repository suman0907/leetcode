class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count , curr = 1, nums[0]
        for i in range(1,len(nums)):
            if nums[i]==curr:
                count +=1
            else:
                count -=1
            if not count:
                curr = nums[i]
                count =1
        return curr            

        