class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        co=0
        c1=0
        c2=0
        for i in nums:
            if i==0:
                co+=1
            elif i==1:
                c1 +=1
            elif i==2:
                c2 +=1
        for i in range(len(nums)):
            if i<co:
                nums[i]=0
            elif i>=co and i<co+c1:
                nums[i]=1
            elif i>=co+c1 and i<co+c1+c2:
                nums[i]=2
                   

        