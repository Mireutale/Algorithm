# PG 42840 모의고사 문제

import sys
input = lambda: sys.stdin.readline().rstrip()

def solution(N, stages):
    stage_fail_cnt = [0] * (N + 1)
    for fail_stage in stages:
        stage_fail_cnt[fail_stage-1] += 1
    fail_rate = dict()
    player = len(stages)
    for i in range(len(stage_fail_cnt[:N])):
        fail_player = stage_fail_cnt[i]
        if player:
            fail_rate[i] = fail_player/player
        if not player:
            fail_rate[i] = 0
        player -= fail_player
    answer = [idx + 1 for idx, rate in sorted(fail_rate.items(), key=lambda x:x[1], reverse=True)]
    return answer

if __name__ == "__main__":
    N = int(input())
    stages = list(map(int, input().split(",")))
    print(solution(N, stages))