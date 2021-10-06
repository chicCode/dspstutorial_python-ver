MAX_ITEMS = 100

class StackType:
    def __init__(self):
        self.info = []

    def is_empty(self):
        return len(self.info)==0
        
    def is_full(self):
        return len(self.info)==MAX_ITEMS
        
    def push(self, item):
        if not self.is_full():
            self.info.append(item)
        else:
            print("Stack is Full")
            exit()

    def pop(self):
        if not self.is_empty():
            return self.info.pop(-1)
        else:
            print("Stack is Empty")
            exit()

    def top(self):
        if not self.is_empty():
            return self.info[-1]
        else:
            print("Stack is Empty")
            exit()
