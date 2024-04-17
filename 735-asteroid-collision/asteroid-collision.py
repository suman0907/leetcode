class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for i in asteroids:
            st.append(i)
            while len(st)>=2 and (st[-1]<0 and st[-2]>0):
                first = st.pop()
                second = st.pop()
                if abs(first)!=abs(second):
                    if abs(first)<abs(second):
                        st.append(second)
                    else:
                        st.append(first)    

        return st               
        