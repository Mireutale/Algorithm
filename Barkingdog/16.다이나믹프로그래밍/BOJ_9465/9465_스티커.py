"""
* CodingTest\Barkingdog\16.다이나믹프로그래밍\BOJ_9465\9465_스티커.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    test_case = int(input())
    for _ in range(test_case):
        n = int(input())
        sticker = [list(map(int, input().split())) for _ in range(2)]
        dp = [[0] * n for _ in range(2)]
        dp[0][0] = sticker[0][0]
        dp[1][0] = sticker[1][0]
        for i in range(1, n):
            dp[0][i] = max(dp[0][i-1], dp[1][i-1] + sticker[0][i], dp[0][i-2] + sticker[0][i])
            dp[1][i] = max(dp[1][i-1], dp[0][i-1] + sticker[1][i], dp[1][i-2] + sticker[1][i])
        print(max(dp[0][n-1], dp[1][n-1]))