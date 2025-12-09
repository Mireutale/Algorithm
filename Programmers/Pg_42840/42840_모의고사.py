# PG 42840 모의고사 문제

import sys
input = lambda: sys.stdin.readline().rstrip()

# 수포자 1 : 1,2,3,4,5 반복, 5개의 수
# 수포자 2 : 2,1,2,3,2,4,2,5 반복, 8개의 수
# 수포자 3 : 3,3,1,1,2,2,4,4,5,5 반복, 10개의 수
def solution(answers):
    answer = []

    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    first_correct = 0
    second_correct = 0
    third_correct = 0

    for i in range(len(answers)):
        # 수포자 1이 정답
        if answers[i]== first[i % len(first)]:
            first_correct += 1
        # 수포자 2가 정답
        if answers[i] == second[i % len(second)]:
            second_correct += 1
        # 수포자 3이 정답
        if answers[i] == third[i % len(third)]:
            third_correct += 1
    correct_max = max(first_correct, second_correct, third_correct)
    if first_correct == correct_max:
        answer.append(1)
    if second_correct == correct_max:
        answer.append(2)
    if third_correct == correct_max:
        answer.append(3)
    return answer

if __name__ == "__main__":
    answers = list(map(int, input().split(",")))
    print(solution(answers))