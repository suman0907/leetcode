class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if i=="(" or i=="{" or i=="[":
                st.append(i)
            elif len(st)==0:
                return False
            elif (i==")" and st[-1]=="(") or (i=="}" and st[-1]=="{") or (i=="]" and st[-1]=="["):
                st.pop()
            else:
                st.append(i)
        return len(st)==0                    
        