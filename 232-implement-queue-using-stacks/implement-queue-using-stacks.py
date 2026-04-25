class MyQueue:

    def __init__(self):
        self.str1=[]
        self.str2 =[]

    def push(self, x: int) -> None:
        self.str1.append(x)

    def pop(self) -> int:
       self.peek()
       return self.str2.pop()

    def peek(self) -> int:
        if not self.str2:
            while self.str1:
                self.str2.append(self.str1.pop())
        return self.str2[-1]

    def empty(self) -> bool:
        return not self.str2 and not self.str1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()