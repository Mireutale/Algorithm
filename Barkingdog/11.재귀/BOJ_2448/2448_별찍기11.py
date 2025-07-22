"""
* CodingTest/Barkingdog/11.재귀/BOJ_2448/2448_별찍기11.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def star_print(row: int, col: int, n: int):
    if n == 3:
        for i in range(row, row + 3):
            for j in range(col, col + 6):
                if i == row:
                    if j == col + 2:
                        ans[i][j] = "*"
                elif i == row + 1:
                    if j == col + 1 or j == col + 3:
                        ans[i][j] = "*"
                else:
                    if j != col + 5:
                        ans[i][j] = "*"
    else:
        n //= 2
        star_print(row, col + n, n)
        star_print(row + n, col, n)
        star_print(row + n, col + n*2, n)

# ! 가독성을 좋게 한 버전
# def star_print(row, col, size):
#     # pattern을 기본적으로 설정
#     if size == 3:
#         pattern = [
#             "  *  ",
#             " * * ",
#             "*****"
#         ]
#         for i in range(3):
#             for j in range(5):
#                 ans[row + i][col + j] = pattern[i][j]
#     else:
#         half = size // 2
#         star_print(row, col + half, half)           # 위쪽 삼각형
#         star_print(row + half, col, half)           # 왼쪽 아래 삼각형
#         star_print(row + half, col + 2*half, half)    # 오른쪽 아래 삼각형

if __name__ == "__main__":
    n = int(input())
    ans = [[' '] * (n*2) for _ in range(n)]
    star_print(0, 0, n)
    for row in ans:
        print(*row, sep='')
