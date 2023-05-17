class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        arr = [0]*len(nums)
        for i in range(len(nums)):
            if arr[nums[i]]:
                return nums[i]
            arr[nums[i]]=nums[i]    
        