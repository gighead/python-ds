from stack import Stack


def string_reverse(word):
    rev = ''
    s = Stack()
    for i in word:
        s.push(i)
    
    print(s.size())
    
    while not s.is_empty():
        rev += s.pop()


    return rev

