class MyHashSet:

    def __init__(self):
        self.mp ={}
        

    def add(self, key: int) -> None:
        self.mp[key]=1
        

    def remove(self, key: int) -> None:
        if key in self.mp:
            del self.mp[key]
        

    def contains(self, key: int) -> bool:
        if key in self.mp:
            return True
        else:
            return False    
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)