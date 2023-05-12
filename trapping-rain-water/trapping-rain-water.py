class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        larr = [0]*n
        rarr = [0]*n
        larr[0]=height[0]
        rarr[n-1]=height[n-1]
        for i in range(1,n,1):
            larr[i] = max(larr[i-1],height[i])
        for i in range(n-2,-1,-1):
            rarr[i]=max(rarr[i+1],height[i])
        water =0
        for i in range(len(height)):
            water +=   abs(min(larr[i],rarr[i])-height[i])  
        return water       
        
        