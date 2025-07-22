"""
* CodingTest/Barkingdog/11.재귀/BOJ_2447/2447_별찍기10.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

# def zero_print(x: int, y: int, size: int):
#     if size > 3:
#         for i in range(3):
#             for j in range(3):
#                 if not (i == 1 and j == 1):
#                     zero_print(x + i * (size//3), y + j * (size//3), size//3)
#                 else:
#                     zero_print(x + i * (size//3), y + j * (size//3), size//3)
#     else:
#         for i in range(3):
#             for j in range(3):
#                 ans[x + i].append(" ")

# def star_print(x: int, y: int, size: int):
#     if size > 3:
#         for i in range(3):
#             for j in range(3):
#                 if not (i == 1 and j == 1):
#                     star_print(x + i * (size//3), y + j * (size//3), size//3)
#                 else:
#                     zero_print(x + i * (size//3), y + j * (size//3), size//3)
#     else:
#         for i in range(3):
#             for j in range(3):
#                 if not (i == 1 and j == 1):
#                     ans[x + i].append("*")
#                 else:
#                     ans[x + i].append(" ")

# if __name__ == "__main__":
#     n = int(input())
#     ans = [[] for _ in range(n)]
#     star_print(0, 0, n)
#     for row in ans:
#         print(*row, sep="")

# ! 리팩토링
def draw_star(x, y, size):
    if size == 1:
        ans[x][y] = '*'
        return

    step = size // 3
    for i in range(3):
        for j in range(3):
            # ? 공백은 그대로 유지
            if i == 1 and j == 1:
                continue
            draw_star(x + i * step, y + j * step, step)

if __name__ == "__main__":
    n = int(input())
    # ? 2차원 배열의 모든 값을 공백으로 초기화
    ans = [[' ' for _ in range(n)] for _ in range(n)]
    draw_star(0, 0, n)
    for row in ans:
        print(''.join(row))
