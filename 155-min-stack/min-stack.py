class MinStack:

    def __init__(self):
        self.st = []
        

    def push(self, val: int) -> None:
        if len(self.st)==0:
            self.st.append([val,val])
        else:
            lastmin = self.st[-1][1]
            if  lastmin <val:
                self.st.append([val,lastmin])
            else:
                self.st.append([val,val])


        

    def pop(self) -> None:
        self.st.pop()
        

    def top(self) -> int:
        return self.st[-1][0]
        

    def getMin(self) -> int:
        return self.st[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()