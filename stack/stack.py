class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def remove(self, item):
        self.items.remove(item)

    def size(self):
        return len(self.items)

    

 
# s = Stack()
# s.push('sai')
# s.push('varun')
# print(s.__dict__)
# print(s.peek())
# # k = s.pop()
# # print
# # print(s.__dict__)
# # print(s.size())
# # # print(s.is_empty())
# # # s.remove('sai')
# # # print(s.is_empty())