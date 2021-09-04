import collections

def solution(p,c):
    p.sort()
    c.sort()
    result = collections.Counter(p)-collections.Counter(c)
    return list(result)[0]
