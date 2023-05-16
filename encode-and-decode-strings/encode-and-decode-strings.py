class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        new_s = ""
        for s in strs:
            new_s +=str(len(s))+"#"+s
        return new_s    
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        ans =[]
        i = 0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            len_s = int(s[i:j])
            new_s = s[j+1:j+1+len_s]
            ans.append(new_s)
            i=j+1+len_s
        return ans       
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))