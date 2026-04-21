# Barkingdog/16.다이나믹프로그래밍/BOJ_2293/2293_동전1.py

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n, k = map(int, input().split())
    coin_value = []
    for _ in range(n):
        coin_value.append(int(input()))
    dp = [[1, -1] for _ in range(n)]
    dp = [0] * (k + 1)
    
    # * i의 가치를 만들 수 있는 방법 = i-coin을 만들 수 있는 방법에 coin을 추가
    for coin in coin_value:
        for i in range(coin, k + 1):
            if i - coin > 0: # ? i - coin이 0보다 크다면, i-coin을 만들 수 있는 가짓수에 coin을 추가하면 됨!!
                dp[i] += dp[i - coin]
            elif i == coin: # ! 만약 i가 coin과 같다면, 새로운 가치의 coin을 사용가능!!
                dp[i] += 1
    print(dp[-1])
