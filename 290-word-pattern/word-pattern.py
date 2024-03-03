class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split(" ")
        if len(pattern)!=len(arr):
            return False
        mp1 = {}
        mp2 = {}
        for i in range(len(pattern)):
            x = pattern[i]
            y = arr[i]
            if (x in mp1 and mp1[x]!=y) or (y in mp2 and mp2[y]!=x):
                return False
            mp1[x]=y
            mp2[y]=x    
        return True

        