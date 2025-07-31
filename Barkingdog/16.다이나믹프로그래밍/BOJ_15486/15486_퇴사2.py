"""
* CodingTest/Barkingdog/16.다이나믹프로그래밍/BOJ_15486/15486_퇴사2.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input())
    work = [list(map(int, input().split())) for _ in range(n)]
    dp = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        time, pay = work[i]
        finish_day = i + time
        if finish_day <= n:
            dp[i] = max(dp[i + 1], dp[finish_day] + pay)
        else:
            dp[i] = dp[i + 1]
    print(dp[0])