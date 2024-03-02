class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        pool = set()
        for i in emails:
            local, domain = i.split("@")
            res = ""
            for j in range(len(local)):
                if local[j]==".":
                    continue
                if local[j]=="+":
                    break
                res +=local[j]
            pool.add(res+"@"+domain) 
        return len(pool)               
        