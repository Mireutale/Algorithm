# Barkingdog/16.다이나믹프로그래밍/BOJ_11053/11053_가장긴증가하는부분수열.py

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input())
    A = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = 1
    for i in range(1, n):
        dp[i] = 1
        for j in range(i):
            if A[j] < A[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))
