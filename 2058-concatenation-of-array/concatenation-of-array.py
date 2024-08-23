class Solution: 
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        j =0
        while j<2:
            for i in range(len(nums)):
                ans.append(nums[i])
            j +=1    

        return ans

          

     