class Solution:
    def searchFirst(self,nums,target):
        l = 0
        r = len(nums)-1
        index = -1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                index= mid
                r= mid-1
            elif nums[mid]>target:
                r = mid-1
            else:
                l = mid+1
        return index 
    def searchLast(self,nums,target):
        l = 0
        r = len(nums)-1
        index = -1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                index= mid
                l = mid+1
            elif nums[mid]>target:
                r = mid-1
            else:
                l = mid+1
        return index

                            
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1,-1]
        result[0]= self.searchFirst(nums,target)
        result[1]= self.searchLast(nums,target)
        return result

        