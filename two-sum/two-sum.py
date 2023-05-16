class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            mp[nums[i]]=i
        for i in range(len(nums)):
            if mp.get(target-nums[i]) and mp.get(target-nums[i])!=i:
                return [mp.get(target-nums[i]),i]
        return [-1,-1]            

        