class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        subset = []
        def dfs(i,subset):
            if i>=len(nums):
                result.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1,subset)
            subset.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i +=1
            dfs(i+1,subset)    




        dfs(0,[])
        return result
        