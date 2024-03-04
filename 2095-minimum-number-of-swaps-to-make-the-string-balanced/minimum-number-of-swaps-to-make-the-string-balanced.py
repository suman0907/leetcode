class Solution:
    def minSwaps(self, s: str) -> int:
        mx = 0
        imblc =0
        for i in s:
            if i=='[':
                imblc -= 1
            else:
                imblc += 1
            mx =max(mx,imblc)
       
        return (mx+1)//2     
        