class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        st = [0]
        for i in range(1, len(temperatures)):
            curr_temp = temperatures[i]
            while len(st)!=0 and temperatures[st[-1]]<curr_temp:
                index = st.pop()
                result[index]=i-index
            st.append(i)
        return result        
                

        