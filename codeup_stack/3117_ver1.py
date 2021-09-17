T = int(input())
stack = []
for i in range(T):
    num = int(input())
    if(num != 0):
        stack.append(num)
    else:
        stack.pop()
print(sum(stack))


# 시간이 너무 오래 걸린다. 
# 해결책
# import sys
# sys.stdin.readline()을 활용해서 반복문으로 입력받을 때 사용한다. 
# ver2 확인
