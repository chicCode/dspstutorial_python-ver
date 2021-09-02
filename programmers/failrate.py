def solution(N:int,Stages:list)->list:
    answer = []
    tmp = []
    c_len = len(Stages)
    for i in range(1,N+1):
        num = Stages.count(i)
        if(num==0):
            f_rate = 0
        else:
            f_rate = num/c_len
        tmp.append([i,f_rate])
        c_len -= num
    tmp.sort(key = lambda x:x[1],reverse=True)
    for i in range(N):
        answer.append(tmp[i][0])
    return answer
