# Barkingdog/9.BFS&10.DFS/BOJ_7562/7562_나이트의이동.py

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

"""
[설계]

나이트가 이동하려고 하는 칸이 주어지는 경우
몇 번 움직이면 이 칸으로 이동 가능한지?
"""

def knight(line, st_x, st_y, f_x, f_y):
    q = deque([(st_x, st_y)])
    visited = [[0] * line for _ in range(line)]

    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [1, -1, 2, -2, 2, -2, 1, -1]

    while q:
        x, y = q.popleft()
        # 정답 위치인지 확인
        if x == f_x and y == f_y:
            return visited[y][x]
        for i in range(8):
            # 이동한 나이트의 위치
            nx = x + dx[i]
            ny = y + dy[i]
            # 체스판 내에 위치할 수 있는 경우, q에 들어가 있지 않은 위치 인 경우
            if 0 <= nx <= line-1 and 0 <= ny <= line-1 and not visited[ny][nx]:
                q.append([nx, ny])
                visited[ny][nx] = visited[y][x] + 1
        
if __name__ == "__main__":
    test_case = int(input())
    for _ in range(test_case):
        chessBoard_line = int(input()) # 4 ~ 300
        kp_y, kp_x = map(int, input().split()) # knight_position
        gp_y, gp_x = map(int, input().split()) # goal_position
        print(knight(chessBoard_line, kp_x, kp_y, gp_x, gp_y))
