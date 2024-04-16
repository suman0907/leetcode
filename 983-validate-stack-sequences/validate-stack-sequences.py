class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []
        j = 0
        for i in pushed:
            st.append(i)
            while len(st)!=0 and  st[-1]==popped[j]:
                st.pop()
                j +=1
        return len(st)==0                  
        