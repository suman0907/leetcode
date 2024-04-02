class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i]==needle[0]:
                temp_s = haystack[i:i+len(needle)]
                if temp_s==needle:
                    return i
        return -1            
        