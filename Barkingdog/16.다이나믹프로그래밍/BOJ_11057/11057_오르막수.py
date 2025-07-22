"""
* CodingTest\Barkingdog\16.다이나믹프로그래밍\BOJ_11057\11057_오르막수.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input())
    dp = list([0] * 10 for _ in range(n + 1))
    for i in range(10):
        dp[1][i] = 1
    
    for i in range(2, n + 1):
        for j in range(10):
            dp[i][j] = sum(dp[i-1][:j+1])
            """
            다른 방법
            for k in range(j + 1):
                dp[i][j] += dp[i-1][k]
            """
    print(sum(dp[n]) % 10007)