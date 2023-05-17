class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_org = (n*(n+1))//2
        return sum_org-sum(nums)
        