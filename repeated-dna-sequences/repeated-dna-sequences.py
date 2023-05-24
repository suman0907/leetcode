class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = set()
        st = set()
        for i in range(len(s)):
            dna = s[i:i+10]
            if dna in st:
                ans.add(dna)
            else:
                st.add(dna)    
        return ans    
        