class Solution:
    def trap(self, height: List[int]) -> int:
        la = [0]*len(height)
        ra = [0]*(len(height))
        la[0] = height[0]
        ra[-1] = height[-1]
        for i in range(1,len(height)):
            la[i]= max(la[i-1],height[i])
        for i in range(len(height)-2,-1,-1):
            ra[i]= max(ra[i+1],height[i]) 
        water = 0
        for i in range(len(height)):
            water +=abs(min(la[i],ra[i])-height[i]) 
        return water         
        