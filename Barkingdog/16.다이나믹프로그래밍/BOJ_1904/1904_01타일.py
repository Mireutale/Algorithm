"""
* CodingTest/Barkingdog/16.다이나믹프로그래밍/BOJ_1904/1904_01타일.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input())
    dp = [0] * n
    for i in range(n):
        if i == 0:
            dp[i] = 1
        elif i == 1:
            dp[i] = 2
        else:
            dp[i] = (dp[i-2] + dp[i-1]) % 15746
    print(dp[-1])