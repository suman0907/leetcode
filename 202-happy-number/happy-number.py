class Solution:
    def squared(self,n):
        sq = 0
        while n:
            rem = n%10
            sq +=pow(rem,2)
            n = n//10
        return sq    

            
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        st = set()
        while n!=1 and n  not in st:
            st.add(n)
            new_n = self.squared(n)
            if new_n==1:
                return True
            n = new_n    
            
        return False        
            

        