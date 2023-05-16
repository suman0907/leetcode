class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mp = {}
        for i in strs:
            s = "".join(sorted(i))
            if s not in mp:
                mp[s]= [i]
            else:
                mp[s].append(i)
        result = []        
        for key,val in mp.items():
            result.append(val)  
        return result              
        