class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mp = {}
        for i in range(len(nums)):
            if nums[i] in mp:
                mp[nums[i]] = mp[nums[i]]+1
            else:
                mp[nums[i]]=1  
        for key, val in mp.items():  
            if val>1:
                return True
        return False        



        

       
        