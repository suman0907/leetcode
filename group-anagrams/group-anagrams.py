class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        mp = {}
        for i in strs:
            s = "".join(sorted(i))
            if s in mp:
                mp[s].append(i)
            else:
                mp[s]=[i]  
        for key,val in mp.items():
            result.append(val)  
        return result            


        