"""
* CodingTest/Barkingdog/16.다이나믹프로그래밍/BOJ_11052/11052_카드구매하기.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input())
    p = [0] + list(map(int, input().split()))
    dp = [0] * (n+1)
    for i in range(1, n+1):
        for j in range(1, i+1):
            dp[i] = max(dp[i], dp[i-j] + p[j])
    print(dp[n])