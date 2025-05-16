"""
* Codes\0x10 다이나믹프로그래밍\BOJ_9095\9095_1,2,3더하기.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()
"""
if __name__ == "__main__":
    T = int(input())
    dp = [0] * (11+1)
    dp[1] = 1 # ? 1을 나타내는 방법, 1
    dp[2] = 2 # ? 2를 나타내는 방법, 1+1, 2
    dp[3] = 4 # ? 3을 나타내는 방법, 1+1+1, 1+2, 2+1, 3
    # 4부터는 1,2,3을 더해서 나타내는 방법을 찾아야 한다.
    for i in range(4, 11+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    for _ in range(T):
        n = int(input())
        print(dp[n])
"""
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        dp = [0] * (11+1)
        dp[0] = 1
        for i in range(1, n+1):
            if i == 1:
                dp[i] = dp[i-1]
            elif i == 2:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        print(dp[n])

