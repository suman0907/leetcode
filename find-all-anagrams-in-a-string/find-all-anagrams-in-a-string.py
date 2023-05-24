class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):
            return []
        mp = {}
        mps = {}
        result = []
        for i in range(len(p)):
            mp[p[i]]= mp.get(p[i],0)+1
            mps[s[i]]= mps.get(s[i],0)+1
        if mp==mps:
            result.append(0)

        l = 0
        r = len(p)
        for r in range(len(p),len(s)):
            mps[s[r]]= mps.get(s[r],0)+1
            mps[s[l]] = mps.get(s[l],0)-1   
            if mps[s[l]]==0:
                mps.pop(s[l])
            if mps==mp:
                result.append(l+1)    
            l +=1  
        return result      
        
        