"""
* CodingTest/Barkingdog/16.다이나믹프로그래밍/BOJ_2240/2240_자두나무.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    T, W = map(int, input().split())
    drop = [0] + [int(input()) for _ in range(T)]
    dp = [[0] * (W + 1) for _ in range(T + 1)]

    # 0 ~ i ~ T
    for i in range(T+1):
        # 1번 나무에서 한 번도 움직이지 않는 경우
        if (drop[i] == 1):
            dp[i][0] = dp[i-1][0] + 1
        else:
            dp[i][0] = dp[i-1][0]

        # 1번 이상 움직이는 경우에 대해 탐색, 1 ~ j ~ W
        for j in range(1, W+1):
            # i초에 2번 나무에서 자두가 떨어지고, 현재 2번 나무에 위치해있다면
            if (drop[i] == 2 and j % 2 == 1):
                # 이전 위치로부터 움직여서 받아 먹을 것인지, 현재 위치에서 받아 먹을 것인지를 비교
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
            # i초에 1번 나무에서 자두가 떨어지고, 현재 1번 나무에 위치해있다면
            elif (drop[i] == 1 and j % 2 == 0):
                # 이전 위치로부터 움직여서 받아 먹을 것인지, 현재 위치에서 받아 먹을 것인지를 비교
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + 1
            # i초에 자두가 떨어지는 나무와 현재 나무의 위치가 다르다면
            else:
                # 움직여서 못 먹는 경우와 움직이지 않아서 못 먹는 경우를 비교
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j])

    # DP 테이블의 마지막 행의 최댓값을 출력
    print(max(dp[T]))
