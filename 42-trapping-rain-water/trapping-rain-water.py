class Solution:
    def trap(self, height: List[int]) -> int:
        arr1 = [0]*len(height)
        arr2 = [0]*len(height)
        arr1[0]=height[0]
        arr2[-1]=height[-1]
        for i in range(1,len(height)):
            arr1[i]= max(arr1[i-1],height[i])
        for i in range(len(height)-2,-1,-1):
            arr2[i]=max(arr2[i+1],height[i])
        water = 0
        for i in range(len(height)):
            water+=abs(min(arr1[i],arr2[i])-height[i])
        return water        