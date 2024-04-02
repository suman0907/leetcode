class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = {}
        for i in range(len(numbers)):
            mp[numbers[i]]=i
        for i in range(len(numbers)):
            if target-numbers[i] in mp and i!=mp[target-numbers[i]]:
                return [i+1,mp[target-numbers[i]]+1]
        return [-1,-1]            
        