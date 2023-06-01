class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {order[i]: i for i in range(len(order))}
        prev = [order_map[i] for i in words[0]]
        for word in words[1:]:
            curr = [order_map[i] for i in word]
            if prev>curr:
                return False
            prev = curr
        return True        
        