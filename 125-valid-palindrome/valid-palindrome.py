class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip(" ")
        res = ""
        for i in s:
            if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=48 and ord(i)<=57) or (ord(i)>=97 and ord(i)<=122):
                res +=i
        res = res.lower()  
        print(res)    
        i = 0
        j = len(res)-1
        while i<j:
            if res[i]!= res[j]:
                return False
            i +=1
            j -=1
        return True            

        