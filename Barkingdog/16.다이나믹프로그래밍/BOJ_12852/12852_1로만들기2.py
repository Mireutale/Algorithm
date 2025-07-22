"""
* CodingTest/Barkingdog/16.다이나믹프로그래밍/BOJ_12852/12852_1로만들기2.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input())  # 입력값 n을 받음
    dp = [0] * (n + 1) # dp[i]: i를 1로 만들기 위한 최소 연산 횟수 저장
    path = [0] * (n + 1) # path[i]: i에 도달하기 직전의 숫자 저장(경로 추적용)

    dp[1] = 0  # 1은 이미 1이므로 연산 횟수는 0
    path[1] = 0 # 1이 되기 전 값은 0

    for i in range(2, n + 1):
        # 1을 빼는 연산
        dp[i] = dp[i - 1] + 1 # 초기값 설정: 1을 빼는 연산을 통해 i를 만들 수 있음
        path[i] = i - 1

        # 3으로 나누는 연산이 가능한 경우, 만약 dp[i // 3] + 1이 현재 dp[i]보다 작으면 업데이트
        if i % 3 == 0 and dp[i // 3] + 1 < dp[i]:
            dp[i] = dp[i // 3] + 1
            path[i] = i // 3

        # 2로 나누는 연산이 가능한 경우, 만약 dp[i // 2] + 1이 현재 dp[i]보다 작으면 업데이트
        if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
            dp[i] = dp[i // 2] + 1
            path[i] = i // 2

    print(dp[n])  # 최소 연산 횟수 출력
    result = []

    while n > 0:
        result.append(n)
        n = path[n]
    print(*result)