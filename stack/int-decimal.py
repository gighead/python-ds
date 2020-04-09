from stack import Stack
from string_reverse import string_reverse

def convert_int_to_bin(dec_num):
    s = Stack()
    binary = ''
    while dec_num > 0:
        rem = dec_num%2 
        s.push(rem)
        dec_num = dec_num//2

    #return all items in stack as str
    while not s.is_empty():
        binary += str(s.pop())
    
    return binary


print(convert_int_to_bin(4))