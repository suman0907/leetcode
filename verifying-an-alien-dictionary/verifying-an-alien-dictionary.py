class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {order[i]:i for i in range(len(order))}
        prev = [order_map[i] for i in words[0]]
        for i in range(1,len(words)):
            curr = [order_map[w] for w in words[i]]
            if curr<prev:
                return False
            prev = curr
        return True        
        