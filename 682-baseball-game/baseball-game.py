class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        for i in operations:
            if i=="+":
                summ = st[-1]+st[-2]
                st.append(summ)
            elif i=="D":
                op = st[-1]*2
                st.append(op) 
            elif i=="C":
                st.pop()
            else:
                st.append(int(i))    
        return sum(st)          
                       
        