# Barkingdog/11.재귀/BOJ_1074/1074_Z.py

import sys
input = lambda: sys.stdin.readline().rstrip()

# def Z(row, col, side, r, c):
#     global visit
#     if side >= 2:
#         next_side = side // 2
#         for x in range(2):
#             for y in range(2):
#                 Z(row + x * (next_side), col + y * (next_side), next_side, r, c)
#     else:
#         map[row][col] = visit
#         if row == r and col == c:
#             print(visit)
#         visit += 1

def z(n, r, c):
    if n == 0:
        return 0
    
    # 4등분한 정사각형의 한 변의 길이
    side = 2 ** (n-1)

    # 4등분한 정사각형의 넓이
    area = side ** 2

    # 현재 (r, c)가 4분면 중 어디에 있는지 판단
    if r < side and c < side:
        return z(n-1, r, c)
    elif r < side and c >= side:
        return area + z(n-1, r, c - side)
    elif r >= side and c < side:
        return 2 * area + z(n-1, r - side, c)
    else:
        return 3 * area + z(n-1, r - side, c - side)

if __name__ == "__main__":
    n, r, c = map(int, input().split())
    # side = 2 ** n
    # map = [[0] * side for _ in range(side)]
    # visit = 0
    # Z(0, 0, side, r, c)
    # print(map[r][c])
    print(z(n, r, c))
