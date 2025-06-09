"""
* CodingTest\Barkingdog\16.다이나믹프로그래밍\BOJ_10844\10844_쉬운계단수.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input())
    # ? dp[i] = 길이가 i인 계단수가 가지는 마지막 값이 0~9인 경우의 수
    dp = [[0] * 10 for _ in range(n + 1)]
    for i in range(1, n+1):
        for j in range(10):
            if i == 1:
                if j != 0:
                    dp[i][j] = 1
            else:
                if j == 0:
                    dp[i][j] = dp[i-1][1]
                elif j == 9:
                    dp[i][j] = dp[i-1][8]
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
    print(sum(dp[n]) % 1000000000)