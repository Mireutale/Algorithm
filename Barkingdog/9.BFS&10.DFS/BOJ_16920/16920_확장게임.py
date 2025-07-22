"""
* CodingTest/Barkingdog/9.BFS&10.DFS/BOJ_16920/16920_확장게임.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

if __name__ == "__main__":
    n, m, player = map(int, input().split())
    player_scale = list(map(int, input().split()))
    board = [list(input()) for _ in range(n)]
    player_place = [0] * (player)
    player_position = []
    for i in range(n):
        for j in range(m):
            if board[i][j] != "." and board[i][j] != "#":
                player_position.append((i, j, int(board[i][j])))
    
    player_position = sorted(player_position, key=lambda x: x[2])

    # 각 플레이어의 딕셔너리를 초기화
    player_queue = {i: deque() for i in range(1, player + 1)}
    # 각 플레이어의 초기 위치를 딕셔너리에 추가
    for pos in player_position:
        x, y, player_num = pos
        player_queue[player_num].append((x, y))
        player_place[player_num-1] += 1

    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while True:
        expanded = False
        for p in range(1, player + 1):
            scale = player_scale[p-1]
            current_queue = player_queue[p]
            next_queue = deque()
            
            for _ in range(scale):
                if not current_queue:
                    break
                    
                for _ in range(len(current_queue)):
                    x, y = current_queue.popleft()
                    
                    for dx, dy in direction:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == ".":
                            board[nx][ny] = str(p)
                            next_queue.append((nx, ny))
                            player_place[p-1] += 1
                            expanded = True
                current_queue = next_queue
            player_queue[p] = next_queue
        
        if not expanded:
            break
    
    print(*player_place)