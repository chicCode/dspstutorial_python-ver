def solution(answers:list)->list:
    result = []
    num1 = [1,2,3,4,5]
    num2 = [2,1,2,3,2,4,2,5]
    num3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0 for _ in range(3)]

    for i, answer in enumerate(answers):
        if answer == num1[i%len(num1)]:
            score[0] += 1
        if answer == num2[i%len(num2)]:
            score[1] += 1
        if answer == num3[i%len(num3)]:
            score[2] += 1

    for i, s in enumerate(score):
        if s == max(score):
            result.append(i+1)

    return result
