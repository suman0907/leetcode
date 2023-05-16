class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp ={}
        max_l = 0
        start =-1
        for i in range(len(s)):
            if s[i] in mp:
                start = max(start,mp[s[i]])
            max_l = max(max_l,i-start)
            mp[s[i]]= i
        return max_l        
        