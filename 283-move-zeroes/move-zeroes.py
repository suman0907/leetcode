class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = -1
        i = 0
        while i<len(nums):
            if nums[i]!=0:
                j +=1
                nums[j],nums[i]=nums[i],nums[j]
            i +=1    

        