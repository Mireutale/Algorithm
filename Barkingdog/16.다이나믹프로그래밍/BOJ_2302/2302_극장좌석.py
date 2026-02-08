# Barkingdog/16.다이나믹프로그래밍/BOJ_2302/2302_극장좌석.py

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input())  # 좌석의 개수
    m = int(input())  # 고정석의 개수
    vip = [int(input()) for _ in range(m)] # 고정석
    
    seats = list()
    start = 0
    for seat in vip:
        seats.append(seat - start -1)
        start = seat
    seats.append(n - start)
    
    dp = [1] * (max(seats) + 1)

    for i in range(2, len(dp)):
        dp[i] = dp[i-1] + dp[i-2]
    
    ans = 0
    for i in seats:
        if ans == 0:
            ans = dp[i]
        else:
            ans *= dp[i]
    print(ans)
