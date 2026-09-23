class StackEx:
    def __init__(self,size):
        self.size = size
        self.stack = [None]*size
        self.top = -1

    def push(self,item):
        if self.size == self.size -1:
            print("Stack Overflow")

        else:
            self.top+=1
            self.stack[self.top] = item
            print(item,"Pushed into the stack")

    def pop(self):
        if self.top == -1:
            print("stack underflow")

        else:
            item = self.stack[self.top]
            self.stack[self.top] = None
            self.top = -1
            print(item,"Popped from stack")
    def peek(self):
        if self.loop == -1:
            print("Stack is empty")

        else:
            print("Top element :",self.stack[self.top])

    def display(self):
        for i in range (self.size-1,-1,-1):
            print(self.stack[i])


        

hi = StackEx(5)
hi.push(23)
hi.push(27)
hi.push(89)
hi.pop()
hi.display()




                  
