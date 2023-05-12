class Solution:
    def reverse(self, x: int) -> int:
        new_n = abs(x)
        s = str(new_n)
        n = int(s[::-1])
        if n>pow(2,31):
            return 0
        return n if x>0 else n*-1    




        