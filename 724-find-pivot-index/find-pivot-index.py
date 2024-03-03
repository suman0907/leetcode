class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rsum = 0
        for i in nums:
            rsum +=i
        lsum = 0
        for i in range(len(nums)):
            rsum -=nums[i]
            if lsum==rsum:
                return i
            lsum +=nums[i]
        return -1            
        