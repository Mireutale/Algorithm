"""
* CodingTest\Barkingdog\0x10 다이나믹프로그래밍\BOJ_14501\14501_퇴사.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input())
    # * Ti, Pi 순서대로 입력
    work = [list(map(int, input().split())) for i in range(n)]
    payment_perDay = [0] * (n+1)
    
    for i in range(n):
        # * i일까지의 최대 금액 갱신
        if payment_perDay[i] < payment_perDay[i-1]:
            payment_perDay[i] = payment_perDay[i-1]
        
        # * i일에 시작하는 상담이 가능한지 확인
        day, pay = i + work[i][0], work[i][1]
        if day > n:  # 퇴사일을 넘어가면 스킵
            continue
        # * 상담이 끝나는 날의 금액 갱신
        payment_perDay[day] = max(payment_perDay[day], payment_perDay[i] + pay)

    print(max(payment_perDay))