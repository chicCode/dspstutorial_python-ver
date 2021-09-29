import os
from SortedType import *

if __name__ == '__main__':
    l = SortedType()
    f = open('./data.txt', 'r')
    line = f.readline()
    while line:
        t = int(line)
        i = ItemType(t)
        l.insert_item(i)
        line = f.readline()
    f.close()

    print("Before:")
    print(l)

    print("After deleting 65:")
    a = ItemType(65)
    l.delete_item(a)
    print(l)
    print()

    a = ItemType(3)
    if l.retrieve_item(a) == True:
        print(str(a) + " is in the list.")
    else:
        print(str(a) + " is not in the list.")

    a = ItemType(77)
    if l.retrieve_item(a) == True:
        print(str(a) + " is in the list.")
    else:
        print(str(a) + " is not in the list.")
