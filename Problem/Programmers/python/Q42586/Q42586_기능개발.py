"""
progresses > 먼저 배포되어야 하는 순서대로 작업의 진도가 적혀있음
speeds > 각 작업의 개발 속도가 적힌 정수 배열

각 배포마다 몇 개의 기능이 배포되는지를 return
"""
from collections import deque

def solution(progresses, speeds):
    answer = []
    deploy = 0
    speeds = deque(speeds)
    while progresses:
        # 진도가 100이 될 때까지 기능 개발 수행
        if progresses[0] < 100:
            if deploy != 0:
                answer.append(deploy)
                deploy = 0
            progresses = deque(x + y for x, y in zip(progresses, speeds))
        else:   
            progresses.popleft()
            speeds.popleft()
            deploy += 1
    answer.append(deploy)            
    return answer

# -------------------------------------------------------------------------------------------------------------------------
# 옛 풀이

import json
import sys
import math
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def solution(progresses, speeds):
    finish = deque([0] for _ in range(len(progresses)))

    # 마감일 계산
    for i in range(len(progresses)):
        """ 구린 연산
        t = 1
        while progresses[i] + speeds[i] * t < 100:
            t += 1
        finish[i] = t
        """
        t = math.ceil((100 - progresses[i]) / speeds[i])
        finish[i] = t

    # 출력
    answer = []
    i, cnt = 0, 1
    temp = finish.popleft()
    while finish:
        if temp < finish[0]:
            answer.append(cnt)
            cnt = 1
            if finish:
                temp = finish.popleft()
        else:
            finish.popleft()
            cnt += 1
    answer.append(cnt)
    return answer