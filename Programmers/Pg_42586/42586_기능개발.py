# PG 12949 기능개발

import json
import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def solution(progresses, speeds):
    finish = deque([0] for _ in range(len(progresses)))

    # 마감일 계산
    for i in range(len(progresses)):
        t = 1
        while progresses[i] + speeds[i] * t < 100:
            t += 1
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

if __name__ == "__main__":
    progresses = json.loads(input())
    speeds = json.loads(input())
    print(solution(progresses, speeds))