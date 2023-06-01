class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        def children(lock):
            res = []
            for i in range(4):
                add_s = lock[:i]+ str((int(lock[i])+1)%10)+lock[i+1:]
                sub_s = lock[:i] +str(((int(lock[i])-1)+10)%10)+ lock[i+1:]
                res.append(add_s)
                res.append(sub_s)
            return res    
                 
        qu = [("0000",0)]
        vis = set(deadends)  
        while qu:
            front = qu.pop(0)
            lock = front[0]
            turn = front[1]
            if lock==target:
                return turn
            vis.add(lock)
            for child in children(lock):
                if child not in vis:
                    vis.add(child)
                    qu.append((child,turn+1))
        return -1            
                  
        