T = int(input())
stack = []
for i in range(T):
    num = int(input())
    if(num != 0):
        stack.append(num)
    else:
        stack.pop()
print(sum(stack))
