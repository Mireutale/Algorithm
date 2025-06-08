"""
* CodingTest\Barkingdog\16.다이나믹프로그래밍\BOJ_1932\1932_정수삼각형.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input())
    dp = [list(map(int, input().split())) for _ in range(n)]
    for i in range(1, n):
        for j in range(len(dp[i])):
            if j == 0:
                dp[i][j] += dp[i-1][j]
            elif j == i:
                dp[i][j] += dp[i-1][j-1]
            else:
                dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

    print(max(dp[n-1]))