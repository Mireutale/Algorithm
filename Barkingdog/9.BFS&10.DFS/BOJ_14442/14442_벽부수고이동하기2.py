"""
* CodingTest/Barkingdog/9.BFS&10.DFS/BOJ_14442/14442_벽부수고이동하기2.py
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

    queue = deque()

    visited[0][0][0] = 1
    queue.append([0, 0, 0])

    while queue:
        # print(queue)
        y, x, crash_cnt = queue.popleft()
        if y == n-1 and x == m-1:
            print(visited[crash_cnt][y][x])
            exit()
        for dy, dx in direction:
            ny, nx = y + dy, x + dx
            # 현재 can_crash가 visited에 저장된 값보다 작다면, 아래 코드 skip!
            if 0 <= ny < n and 0 <= nx < m:
                if board[ny][nx] == 0 and not visited[crash_cnt][ny][nx]:
                    visited[crash_cnt][ny][nx] = visited[crash_cnt][y][x] + 1
                    queue.append([ny, nx, crash_cnt])
                else:
                    if crash_cnt < crash and not visited[crash_cnt+1][ny][nx]:
                        visited[crash_cnt+1][ny][nx] = visited[crash_cnt][y][x] + 1
                        queue.append([ny, nx, crash_cnt + 1])
    
    print(-1)