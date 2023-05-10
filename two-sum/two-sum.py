class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i in range(len(nums)):
            mp[nums[i]]=i
        for i in range(len(nums)):
            if mp.get(target-nums[i]) and i!=mp.get(target-nums[i]):
                return[i,mp.get(target-nums[i])]
        return [-1,-1]
        