class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mp = {}
        for i , k in enumerate(order):
            mp[k]=i
        
        prev = list(mp[i] for i in words[0])  
        for i in range(1, len(words)):
            curr = list(mp[j] for j in words[i])
            print(curr,prev)
            if curr<prev:
                return False
            prev = curr
        return True         
