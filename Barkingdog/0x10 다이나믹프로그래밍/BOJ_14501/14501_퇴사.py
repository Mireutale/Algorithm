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
    ans = 0
    for i in range(n+1):
        payment_perDay[i] = max(payment_perDay[:i+1])
        day, pay = i + work[i][0], work[i][1]
        if day > n:
            continue
        payment_perDay[day] = max(payment_perDay[day], payment_perDay[i] + pay)
    print(max(payment_perDay))

"""
commit msg
Solved / Working

- Body

Date : [25/05/23] 
"""