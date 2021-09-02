first = [1,4,7]
second = [2,5,8]
third = [3,6,9]
def make_to(a:int)->list:
    answer = []
    if(a in first):
        answer = [(a-1)//3,1]
    elif(a in second):
        answer = [(a-2)//3,2]
    elif(a in third):
        answer = [(a-3)//3,3]
    else:
        answer = [3,2]
    return answer

def solution(numbers:list,hand:list)->str:
    answer = ''
    temp1 = 0
    temp2 = 0
    left = [3,1]
    right = [3,3]
    for i in range(len(numbers)):
        if(numbers[i] in first):
            answer += "L"
            left = make_to(numbers[i])
        elif(numbers[i] in third):
            answer += "R"
            right = make_to(numbers[i])
        else:
            for j in range(2):
                temp1 += abs(make_to(numbers[i])[j]-left[j])
                temp2 += abs(make_to(numbers[i])[j]-right[j])
            if(temp1==temp2):
                if(hand=='right'):
                    right = make_to(numbers[i])
                    answer += 'R'
                else:
                    left = make_to(numbers[i])
                    answer += 'L'
            elif(temp1>temp2):
                right = make_to(numbers[i])
                answer += 'R'
            else:
                left = make_to(numbers[i])
                answer += 'L'
        temp1 = 0
        temp2 = 0
    return answer
