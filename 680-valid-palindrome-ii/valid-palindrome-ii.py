class Solution:
    def isPalindrome(self,new_s):
        i = 0
        j = len(new_s)-1
        while i<j:
            if new_s[i]!=new_s[j]:
                return False
            i +=1
            j -=1
        return True     
    def validPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        new_s = ""
        while i<j:
            if s[i]!=s[j]:
                new_s = s[i:j+1]
                break
            i +=1
            j -=1    
        return self.isPalindrome(new_s[1:]) or self.isPalindrome(new_s[:-1])

        