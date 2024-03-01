class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.mp = {}
        

    def insert(self, val: int) -> bool:
        if val not in self.mp:
            self.arr.append(val)
            self.mp[val]=len(self.arr)-1
            return True
        else:
            return False    
        

    def remove(self, val: int) -> bool:
        if val not in self.mp:
            return False
        else:
            index= self.mp[val]
            lastElement = self.arr[-1]
            self.arr[index]= lastElement
            self.arr[-1]=val
            self.mp[lastElement]= index
            self.arr.pop()
            del self.mp[val]
            return True

        

    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()