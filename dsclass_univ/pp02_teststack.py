import os
from StackType import *

if __name__ == '__main__':
    my_stack = StackType()
    
    for i in range(5):
        number = int(input("enter the number: "))
        my_stack.push(number)
    
    print()
    print(my_stack.is_full())
    print()
    
    while (True):
        if (my_stack.is_empty() == True):
            break
        else:
            print(my_stack.top())
            my_stack.pop()

    print()
    print(my_stack.top())
