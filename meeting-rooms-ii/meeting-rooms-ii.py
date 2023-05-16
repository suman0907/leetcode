class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_arr = []
        end_arr = []
        for i in intervals:
            start_arr.append(i[0])
            end_arr.append(i[1])
        start_arr.sort()
        end_arr.sort()
        i = 0
        j = 0
        total =0
        count = 0
        while i<len(start_arr):
            if start_arr[i]<end_arr[j]:
                count +=1
                i +=1
            else:
                count -=1
                j+=1
            total = max(count,total)    

        return total            
            
    
        