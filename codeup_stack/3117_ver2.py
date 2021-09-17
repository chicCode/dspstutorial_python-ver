import sys
T = int(input())
stack = []
for i in range(T):
    num = int(sys.stdin.readline())
    if(num != 0):
        stack.append(num)
    else:
        stack.pop()
print(sum(stack))
