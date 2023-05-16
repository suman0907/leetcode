class Solution:
    def palindrome(self,s):
        i =0
        j = len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return False
            i +=1
            j -=1

        return True        
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for i in s:
            if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122) or (ord(i)>=48 and ord(i)<=57):
                new_s +=i
        new_s = new_s.lower() 
        return self.palindrome(new_s)       
                
        