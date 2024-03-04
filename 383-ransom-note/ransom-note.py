class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mp1 = {}
        mp2 = {}
        for i in ransomNote:
            mp1[i]= mp1.get(i,0)+1
        for i in magazine:
            mp2[i]= mp2.get(i,0)+1  
        for k,v in mp1.items():
            if k not in mp2:
                return False
            elif k in mp2 and mp2[k]<v:
                return False
        return True                

        