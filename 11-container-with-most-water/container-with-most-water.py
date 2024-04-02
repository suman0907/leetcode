class Solution:
    def maxArea(self, height: List[int]) -> int:
        area =0
        i = 0
        j = len(height)-1
        while i<j:
            temp_a = (j-i)*min(height[i],height[j])
            area = max(area,temp_a)
            if height[i]>height[j]:
                j -=1
            else:
                 i+=1
        return area             

        