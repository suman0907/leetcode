class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr = [1]
        fp =1
        for i in range(1,len(nums)):
            fp*= nums[i-1]
            arr.append(fp)
        bp = 1
        for i in range(len(nums)-2,-1,-1):
            bp *=nums[i+1]
            arr[i]=arr[i]*bp

        return arr        
        