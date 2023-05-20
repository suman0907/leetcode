from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        arr = [(-val,key) for key,val in count.items()]
        heapq.heapify(arr)
        res = [heapq.heappop(arr)[1] for _ in range(k)]
        return res
        

        