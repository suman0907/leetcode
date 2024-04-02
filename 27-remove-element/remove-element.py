class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j =-1
        i =0
        while i<len(nums):
            if nums[i]!=val:
                j+=1
                nums[j]=nums[i]
            i +=1
        return j+1        
        