class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)==0:
            return []
        start = nums[0]
        end = float("inf")
        result = []
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]!=1:
                end = nums[i-1]
                if start==end:
                    result.append(f"{start}")
                else:    
                    result.append(f"{start}->{end}")
                start = nums[i] 
            end = nums[i]    

        if start==end or end==float("inf"):
            result.append(f"{start}")
        else:    
            result.append(f"{start}->{end}")        
        return result          

        