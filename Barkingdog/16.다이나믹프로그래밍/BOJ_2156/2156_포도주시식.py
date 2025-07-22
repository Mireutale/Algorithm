"""
* CodingTest/Barkingdog/16.다이나믹프로그래밍/BOJ_2156/2156_포도주시식.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input())
    glasses = [int(input()) for _ in range(n)]
    dp = [0] * n
    for i in range(n):
        if i == 0:
            dp[0] = glasses[0]
        elif i == 1:
            dp[1] = glasses[0] + glasses[1]
        elif i == 2:
            dp[2] = max(glasses[0] + glasses[2], dp[1], glasses[1] + glasses[2])
        else: # 점화식
            dp[i] = max(dp[i-2] + glasses[i], dp[i-1] , dp[i-3] + glasses[i-1] + glasses[i])
    print(dp[n-1])