from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        arr = [(-val,key) for key,val in count.items()]
        heapq.heapify(arr)

        result = ""
        p_a = ""
        p_b = 0
        while arr:
            top = heapq.heappop(arr)
            a = top[1]
            b = top[0]
            result +=a
            if p_b<0:
                heapq.heappush(arr,(p_b,p_a))
            b +=1
            p_a = a
            p_b = b
        return result if len(result)==len(s) else ""  


        