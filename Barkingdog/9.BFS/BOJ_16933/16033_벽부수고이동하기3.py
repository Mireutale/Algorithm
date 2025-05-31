"""
* Barkingdog\0x09 BFS\BOJ_16933\16033_벽부수고이동하기3.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

if __name__ == "__main__":
    n, m, crash = map(int, input().split())
    board = [list(map(int, input())) for _ in range(n)]
    
    visited = [[[0] * m for _ in range(n)] for _ in range(crash+1)]
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    visited[0][0][0] = 1
    queue = deque()
    queue.append([0, 0, 0, 1]) # y, x, 벽을 깬 횟수, 거리

    while queue:
        # print(queue)
        y, x, crash_cnt, distance = queue.popleft()
        if y == n-1 and x == m-1:
            print(distance)
            exit()
        day_or_night = distance % 2 # 1이면 낮, 0이면 밤
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            # 현재 can_crash가 visited에 저장된 값보다 작다면, 아래 코드 skip!
            if 0 <= ny < n and 0 <= nx < m:
                # 빈 공간
                if board[ny][nx] == 0 and not visited[crash_cnt][ny][nx]:
                    visited[crash_cnt][ny][nx] = visited[crash_cnt][y][x] + 1
                    queue.append([ny, nx, crash_cnt, distance + 1])
                # 벽
                if board[ny][nx] == 1 and crash_cnt < crash and not visited[crash_cnt+1][ny][nx]:
                    if day_or_night: # 아침
                        visited[crash_cnt+1][ny][nx] = visited[crash_cnt][y][x] + 1
                        queue.append([ny, nx, crash_cnt + 1, distance + 1])
                    else: # 밤
                        queue.append([y, x, crash_cnt, distance + 1])
    
    print(-1)


# commit msg
# --- 문제풀이_mireutale[25/ / ]