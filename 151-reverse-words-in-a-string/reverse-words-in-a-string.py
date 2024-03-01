class Solution:
    def reverseWords(self, s: str) -> str:
        s= s.strip(" ") 
        arrs = s.split()
        i = 0
        j = len(arrs)-1
        while i<j:
            arrs[i],arrs[j]=arrs[j],arrs[i]
            i+=1
            j-=1
        return " ".join(arrs)
        