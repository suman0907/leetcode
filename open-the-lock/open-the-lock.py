class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        def children(lock):
            res = []
            for i in range(4):
                add_s = lock[:i]+str((int(lock[i])+1)%10)+lock[i+1:]
                sub_s = lock[:i]+str(((int(lock[i])-1)+10)%10)+lock[i+1:]
                res.append(add_s)
                res.append(sub_s)
            return res    
                


        q = [["0000",0]]
        vis = set(deadends)
        while q:
            lock, turn = q.pop(0)
            if lock==target:
                return turn
            for child in children(lock):
                if child not in vis:
                    q.append([child,turn+1])
                    vis.add(child) 
        return -1               

