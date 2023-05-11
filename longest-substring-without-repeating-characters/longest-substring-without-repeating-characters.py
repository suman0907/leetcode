class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        start = -1
        max_len = 0
        mp = {}
        for i in range(len(s)):
            if s[i] in mp:
                start = max(start,mp[s[i]])
            max_len = max(i-start,max_len)        
            mp[s[i]]=i
        return max_len        

        