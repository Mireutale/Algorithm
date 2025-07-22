"""
* CodingTest/Barkingdog/16.다이나믹프로그래밍/BOJ_11726/11726_2xn타일링.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input())
    dp = [1] * (n + 1)
    for i in range(1, n+1):
        if i > 1:
            dp[i] = dp[i-1] + dp[i-2]
    print(dp[i] % 10007)