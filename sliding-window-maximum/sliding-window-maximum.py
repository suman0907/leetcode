from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        d = deque()
        for i in range(len(nums)):
            while d and d[0]<=i-k:
                d.popleft()
            while d and nums[i]>nums[d[-1]]:
                d.pop()
            d.append(i)
            if i>=k-1:
                result.append(nums[d[0]])
        return result                

        