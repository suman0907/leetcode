class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        mp1 = {}
        mp2 = {}
        for i in range(len(s)):
            x = s[i]
            y = t[i]
            if (x in mp1 and mp1[x]!=y) or (y in mp2 and mp2[y]!=x):
                return False
            mp1[x]=y
            mp2[y]=x
        return True    
        