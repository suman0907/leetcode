class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i]==needle[0]:
                cs = haystack[i:i+len(needle)]
                print(cs)
                if cs==needle:
                    return i
        return -1            

        