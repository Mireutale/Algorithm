"""
* CodingTest\Barkingdog\16.다이나믹프로그래밍\BOJ_11055\11055_가장큰증가하는부분수열.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input())
    A = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = A[0]
    for i in range(1, n):
        dp[i] = A[i]
        for j in range(i):
            if A[i] > A[j]:
                dp[i] = max(dp[i], dp[j] + A[i])
    print(max(dp))