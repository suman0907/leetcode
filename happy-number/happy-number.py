class Solution:
    def findSquare(self,n):
        square = 0
        while n:
            rem = n%10
            square +=pow(rem,2)
            n = n//10
        return square    

    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        st = set()
        while n!=1 and n not in st:
            st.add(n)
            new_n = self.findSquare(n)
            if new_n==1:
                return True
            n = new_n
        return False   


        