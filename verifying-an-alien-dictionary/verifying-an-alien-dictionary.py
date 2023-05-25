class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mp = {}
        for i,v in enumerate(order):
            mp[v]=i
        prev = [mp[i] for i in words[0]] 
        for i in range(1,len(words)):
            curr = [mp[i] for i in words[i]] 
            if prev>curr:
                return False
            prev = curr
        return True          


        