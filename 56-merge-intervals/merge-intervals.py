class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        result = [intervals[0]]
        for intr in intervals[1:]:
            last = result[-1]
            if intr[0]<=last[1]:
                result[-1][0] = min(intr[0],last[0])
                result[-1][1] = max(intr[1],last[1])
            else:
                result.append(intr) 
        return result           

        