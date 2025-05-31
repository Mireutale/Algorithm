"""
* CodingTest\Barkingdog\16.다이나믹프로그래밍\BOJ_15988\15988_1,2,3더하기3.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    test_case = int(input())
    dp = [0] * 1000000
    dp[0] = 1
    dp[1] = 2
    dp[2] = 4
    for i in range(3, 1000000):
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009
    for _ in range(test_case):
        n = int(input())
        print(dp[n-1])