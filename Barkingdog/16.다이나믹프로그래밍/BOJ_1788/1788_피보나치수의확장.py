"""
* CodingTest/Barkingdog/16.다이나믹프로그래밍/BOJ_1788/1788_피보나치수의확장.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    limit_num = 1000000000
    n = int(input())
    dp = [0] * (abs(n)+1)
    if abs(n) >= 1:
        dp[1] = 1
    for i in range(2, abs(n) + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % limit_num
    
    if n < 0 and n % 2 == 0:
        print(-1)
        print(dp[-1])
    else:
        if n == 0:
            print(0)
        else:
            print(1)
        print(dp[-1])