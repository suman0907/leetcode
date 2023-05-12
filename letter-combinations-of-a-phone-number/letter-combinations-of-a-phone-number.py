from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        mp = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"

        }
        temp_l = []
        for d in digits:
            temp_l.append(mp[d])
        prod = product(*temp_l)
        result = []
        for p in list(prod):
            if p =="":
                continue
            s = "".join(p)    
            result.append(s)    
        
        return result


        