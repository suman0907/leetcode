class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        la = [0]*n
        ra =[0]*n
        la[0]=height[0]
        ra[n-1]=height[-1]
        for i in range(1,n,1):
            la[i]=max(la[i-1],height[i])
        for i in range(n-2,-1,-1):
            ra[i]=max(ra[i+1],height[i])
        water =0
        for i in range(n):
            water += abs(min(la[i],ra[i])-height[i]) 
        return water           
