"""
* CodingTest/Barkingdog/16.다이나믹프로그래밍/BOJ_2579/2579_계단오르기.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    num_of_stairs = int(input())
    stairs = [int(input()) for _ in range(num_of_stairs)]

    dp = [0] * num_of_stairs # 계단 오르기 경로의 최대 점수

    # 초기 조건
    dp[0] = stairs[0]
    for i in range(1, num_of_stairs):
        if i == 1:
            dp[i] = stairs[0] + stairs[1]
        elif i == 2:
            dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
        else:
            # 두 계단 점프 or 이전 두 계단 점프 + 한 계단 점프
            # 마지막 계단은 위치해야 하므로, start[i]를 포함
            dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

    print(dp[num_of_stairs-1])