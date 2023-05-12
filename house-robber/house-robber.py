class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        arr = [0]*len(nums)
        arr[0]=nums[0]
        arr[1]=max(nums[1],nums[0])
        for i in range(2,len(arr)):
            arr[i] = max(arr[i-2]+nums[i],arr[i-1])
        return arr[-1]    
        