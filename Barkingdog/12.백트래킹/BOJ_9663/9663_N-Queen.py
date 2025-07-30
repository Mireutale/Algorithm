"""
* CodingTest/Barkingdog/12.백트래킹/BOJ_9663/9663_N-Queen.py
* Author : mireutale
"""

"""Pypy3으로 풀리는 문제
import sys
input = lambda: sys.stdin.readline().rstrip()

def safe(row, col) -> bool:
    for i in range(len(queens)):
        if abs(row - i) == abs(col - queens[i]):
            return False
    return True

def N_Queen(row):
    global ans
    if row == n:
        ans += 1
        return

    for col in range(n):
        if col not in queens:
            if safe(row, col):
                queens.append(col)
                N_Queen(row + 1)
                queens.pop()


if __name__ == "__main__":
    n = int(input())
    ans = 0
    queens = []
    N_Queen(0)
    print(ans)
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def N_Queen(row):
    global ans
    if row == n:
        ans += 1
        return

    for col in range(n):
        # 같은 열 또는 대각선에 있지 않은 경우
        if not cols[col] and not right_diagonal[row + col] and not left_diagonal[row - col + n - 1]:
            cols[col] = right_diagonal[row + col] = left_diagonal[row - col + n - 1] = True
            N_Queen(row + 1)
            cols[col] = right_diagonal[row + col] = left_diagonal[row - col + n - 1] = False

if __name__ == "__main__":
    n = int(input())
    ans = 0
    cols = [False] * n # 세로 열
    right_diagonal= [False] * (2 * n - 1) # 오른쪽 대각선
    left_diagonal = [False] * (2 * n - 1) # 왼쪽 대각선
    N_Queen(0)
    print(ans)
