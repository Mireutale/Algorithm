# Problem/Programmers/python/Q131128/Q131128_숫자짝궁.py

import sys
input = lambda: sys.stdin.readline().rstrip()

def cnt_nums(data):
    arr = [0] * 10
    for i in str(data):
        arr[int(i)] += 1
    return arr
    
def solution(X, Y):
    # 0부터 9까지 수 카운트
    num_x = cnt_nums(X)
    num_y = cnt_nums(Y)
    
    # 공통된 수를 합쳐서 common 리스트 생성
    common = [min(x, y) for x, y in zip(num_x, num_y)]
    
    answer = ''
    # 공통된 수가 없는 경우
    if sum(common) == 0:
        return "-1"
    
    # 공통된 수가 0밖에 없는 경우
    if sum(common) == common[0]:
        return "0"
    
    for i in range(10 - 1, -1, -1):
        answer += str(i) * common[i]
    return answer
