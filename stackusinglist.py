class Stack:
    def __init__(self,size=5):
        self.size=size
        self.st=[]
    def push(self,data):
        if len(self.st)==self.size:
            return ValueError("Stack is full")
        else:
            self.st.append(data)
    def pop(self):
        if len(self.st)==0:
            return ValueError("Stack is empty")
        else:
            self.st.pop()
    def peek(self):
        return self.st[-1]
    def display(self):
        return self.st
s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.pop()
s.push(60)
print(s.peek())
print(s.display())
s.push(70)