class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip(" ")
        res =0
        for i in range(len(s)-1,-1,-1):
            if s[i-1]==" ":
                return res+1
            res +=1
        return res        

        