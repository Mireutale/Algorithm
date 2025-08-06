"""
* CodingTest/Barkingdog/12.백트래킹/BOJ_1799/1799_비숍.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def back_tracking(candidate, used1, used2, index, cnt):
    global ans
    if index == len(candidate):
        ans = max(ans, cnt)
        return
    x, y = candidate[index]
    d1 = x + y
    d2 = x - y + (n - 1)

    if not used1[d1] and not used2[d2]:
        used1[d1] = used2[d2] = True
        back_tracking(candidate, used1, used2, index + 1, cnt + 1)
        used1[d1] = used2[d2] = False

    back_tracking(candidate, used1, used2, index + 1, cnt)

if __name__ == "__main__":
    n = int(input())
    board = [] # 전체 체스판
    black = [] # 검은색 칸에 놓을 수 있는 후보지
    white = [] # 흰색 칸에 놓을 수 있는 후보지

    for i in range(n):
        row = list(map(int, input().split()))
        board.append(row)
        for j in range(n):
            if row[j] == 1:
                if (i + j) % 2 == 0:
                    black.append((i, j))
                else:
                    white.append((i, j))

    ans = 0
    back_tracking(black, [False]*2*n, [False]*2*n, 0, 0)
    black_max = ans

    ans = 0
    back_tracking(white, [False]*2*n, [False]*2*n, 0, 0)
    white_max = ans

    print(black_max + white_max)