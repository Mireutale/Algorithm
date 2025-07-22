"""
* CodingTest/Barkingdog/11.재귀/BOJ_2448/2448_별찍기11.py
* Author : mireutale
"""

import sys
import math
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

if __name__ == "__main__":
    n = int(input())
    ans = [[' '] * (n*2) for _ in range(n)]
    star_print(0, 0, n)
    for row in ans:
        print(*row, sep='')