"""
* CodingTest/Barkingdog/13.시뮬레이션/BOJ_21610/21610_마법사 상어와 비바라기.py
* Author : mireutale
"""
import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [] # 기존의 땅 상황
    move = deque() # 구름의 이동
    cloud = deque([[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]])
    for _ in range(N):
        board.append(list(map(int ,input().split())))
    for _ in range(M):
        move.append(list(map(int, input().split())))
    # 8개 방향 : ←(9시), ↖(11시), ↑(12시), ↗(1시), →(3시), ↘(5시), ↓(6시), ↙(7시) 
    direction = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
    diagonal = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    while move:
        direct, move_times = move.popleft()
        for _ in range(len(cloud)):
            x, y = cloud.popleft()
            dx, dy = direction[direct-1]
            nx, ny = x + (dx * move_times), y + (dy * move_times)
            cloud.append([nx % N, ny % N])

        for i, j in cloud:
            board[i][j] += 1
            for k, l in diagonal:
                di, dj = i + k, j + l
                if 0 <= di < N and 0 <= dj < N:
                    if board[di][dj] != 0 or [di, dj] in cloud:
                        board[i][j] += 1
        
        temp = deque()
        for i in range(N):
            for j in range(N):
                if [i, j] not in cloud:
                    if board[i][j] >= 2:
                        board[i][j] -= 2
                        temp.append([i, j])
        cloud = temp
    
    ans = 0
    for i in range(N):
        ans += sum(board[i])
    print(ans)
