class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len(s)!=len(pattern):
            return False
        mp1 = {}
        mp2 = {}
        for i in range(len(pattern)):
            x = pattern[i]
            y = s[i]
            if (x in mp1 and mp1[x]!=y) or (y in mp2 and mp2[y]!=x):
                return False
            mp1[x]=y
            mp2[y]=x
        return True    
        