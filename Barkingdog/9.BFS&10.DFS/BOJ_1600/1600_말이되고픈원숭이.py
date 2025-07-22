"""
* CodingTest/Barkingdog/9.BFS&10.DFS/BOJ_1600/1600_말이되고픈원숭이.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def bfs(horse_move_count):
    queue = deque()
    # visited[y][x][k] : (y,x) 위치에 말 이동 횟수 k로 방문했는지 체크
    visited = [[[False] * (horse_move_count + 1) for _ in range(width)] for _ in range(height)]
    queue.append((0, 0, horse_move_count, 0))
    visited[0][0][horse_move_count] = True
    
    while queue:
        y, x, k, count = queue.popleft()
        if y == height - 1 and x == width - 1:
            return count
            
        # 일반 이동
        for i in range(4):
            ny, nx = y + direction[i][0], x + direction[i][1]
            if 0 <= ny < height and 0 <= nx < width and board[ny][nx] == 0 and not visited[ny][nx][k]:
                visited[ny][nx][k] = True
                queue.append((ny, nx, k, count + 1))
                
        # 말 이동
        if k > 0:
            for i in range(8):
                ny, nx = y + horse_move[i][0], x + horse_move[i][1]
                if 0 <= ny < height and 0 <= nx < width and board[ny][nx] == 0 and not visited[ny][nx][k-1]:
                    visited[ny][nx][k-1] = True
                    queue.append((ny, nx, k-1, count + 1))
    return -1

if __name__ == "__main__":
    # 나이트 이동
    horse_move = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)] 
    # 인접 방향 이동
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    horse_move_count = int(input())
    width, height = map(int, input().split()) #가로, 세로
    board = [list(map(int, input().split())) for _ in range(height)]
    
    print(bfs(horse_move_count))