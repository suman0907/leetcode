class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        for i in range(len(haystack)):
            if haystack[i]==needle[0]:
                new_s = haystack[i:i+n]
                if new_s== needle:
                    return i
        return -1            

                
        