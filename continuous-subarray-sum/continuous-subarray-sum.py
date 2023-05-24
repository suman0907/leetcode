class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mp = {0:-1}
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum +=nums[i]
            rem = prefix_sum%k
            if rem not in mp:
                mp[rem]=i
            elif i-mp[rem]>1:
                return True
        return False            

        