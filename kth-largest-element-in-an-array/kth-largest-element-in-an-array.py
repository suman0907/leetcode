import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr =[]
        for i in nums:
            if len(arr)<k:
                heapq.heappush(arr,i)
            else:
                if i>arr[0]:
                    heapq.heappop(arr)
                    heapq.heappush(arr,i)    
        return arr[0]