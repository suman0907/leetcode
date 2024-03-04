class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        mp1 = {}
        mp2 = {}
        for i in s:
            mp1[i]= mp1.get(i,0)+1
        for i in t:
            mp2[i]=mp2.get(i,0)+1  
        for k,v in mp2.items():
            if k not in mp1:
                return False
            elif mp1[k]<v:
                return False
        return True        

        