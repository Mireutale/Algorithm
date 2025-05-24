"""
* Barkingdog\0x10 다이나믹프로그래밍\BOJ_1463\1463_1로만들기.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    x = int(input())
    dp = [0] * (x + 1) #1을 만들기 위한 최소 연산 횟수

    for i in range(2, x + 1):
        dp[i] = dp[i - 1] + 1  # 1을 빼는 경우
        
        if i % 2 == 0:  # 2로 나누어 떨어지는 경우
            dp[i] = min(dp[i], dp[i // 2] + 1)
            
        if i % 3 == 0:  # 3으로 나누어 떨어지는 경우
            dp[i] = min(dp[i], dp[i // 3] + 1)

    print(dp[x])