"""
* CodingTest/Barkingdog/13.시뮬레이션/BOJ_21610/21610_마법사 상어와 비바라기.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = []
    move = []
    for _ in range(N):
        board.append(list(map(int ,input().split())))
    for _ in range(M):
        move.append(list(map(int, input().split())))
    direction = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    