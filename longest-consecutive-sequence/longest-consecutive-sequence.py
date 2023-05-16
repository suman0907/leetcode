class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_l = 0
        st = set(nums)
        for i in range(len(nums)):
            if nums[i]-1 not in st:
                number = nums[i]+1
                count = 1
                while number in st:
                    count +=1
                    number +=1
                max_l = max(count,max_l)
        return max_l            
                

        