dict = {"one":1,"two":2,"three":3,"four":4,
"five":5,"six":6,"seven":7,"eight":8,"nine":9,"zero":0}


def solution(s:str)->str:
    answer = ""
    tmp = ""
    for i in range(len(s)):
        if(s[i].isdigit()!=True):
            tmp += s[i]
        else:
            answer += s[i]
        if(tmp in dict):
            answer += str(dict[tmp])
            tmp = ""
    return int(answer)
