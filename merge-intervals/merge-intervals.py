class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x:x[0])
        output = [intervals[0]]
        for key in intervals[1:]:
            last_val = output[-1][1]
            if key[0]<=last_val:
                output[-1][1]= max(output[-1][1],key[1])
                output[-1][0]= min(output[-1][0],key[0])
            else:
                output.append(key)
        return output            

        