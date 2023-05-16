from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits =="":
            return []
        phone_map = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        temp_list = []
        for i in digits:
            temp_list.append(phone_map[i])
        prod =   product(*temp_list)  
        result = []
        for p in list(prod):
            if p =="":
                continue
            s = "".join(p)    
            result.append(s)
        return result    
        