class Solution:
    def firstUniqChar(self, s: str) -> int:
        mp = {}
        for i in range(len(s)):
            if s[i] not in mp:
                mp[s[i]]=1
            else:
                mp[s[i]]= int(mp[s[i]])+1

        for i in range(len(s)):
            if s[i] in mp and mp[s[i]]==1:
                return i
        return -1        
                 
        
