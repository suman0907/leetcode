class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = strs[0]
        res = ""
        for i in range(len(s)):
            for j in strs:
                if len(j)<=i or s[i]!=j[i]:
                    return res
            res +=s[i] 
        return res           
                
        