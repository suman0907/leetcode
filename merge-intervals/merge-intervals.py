class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x:x[0])
        output = [intervals[0]]
        for i in intervals[1:]:
            last_val = output[-1][1]
            if i[0]<=last_val:
                output[-1][1]= max(output[-1][1],i[1])
                output[-1][0] = min(output[-1][0],i[0])
            else:
                output.append(i)
        return output            



        