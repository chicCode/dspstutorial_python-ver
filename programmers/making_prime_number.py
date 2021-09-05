from itertools import combinations
def solution(nums:list)->int:
    count = 0
    sum = 0
    temp = list(combinations(nums,3))
    for i in range(len(temp)):
        for j in range(3):
            sum = sum + temp[i][j]
        if(isPrime(sum)==True):
            count = count+1
        sum = 0
    return count

def isPrime(num:int)->bool:
    L = []
    for i in range(2,num):
        if(num%i==0):
            return False
    return True
