class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k>len(nums):
            k = k%len(nums)
        nums.reverse()
        i = 0
        j = k-1
        while i<j:
            nums[i],nums[j]= nums[j],nums[i]
            i +=1
            j -=1
        i = k
        j= len(nums)-1
        while i<j:
            nums[i],nums[j]= nums[j],nums[i]
            i +=1
            j -=1        
        