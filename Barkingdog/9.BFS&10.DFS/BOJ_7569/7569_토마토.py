"""
* CodingTest/Barkingdog/9.BFS&10.DFS/BOJ_7569/7569_토마토.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

"""
[설계]
7567 토마토 문제와 비슷
대신, 상하좌우 에서 추가적으로 앞뒤 6방향 -> 3차원으로 확장

전체 box를 확인해서 익은 토마토를 queue에 입력
"""

if __name__ == "__main__":
    m, n, h = map(int, input().split())
    box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
    queue = deque()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if box[i][j][k] == 1:
                    queue.append([i, j, k])
    
    while queue:
        x, y, z = queue.popleft()
        # 앞 뒤 상 하 좌 우
        direction = ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1))
        for i in range(6):
            nx, ny, nz = x + direction[i][0], y + direction[i][1], z + direction[i][2]
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
                if box[nx][ny][nz] == 0:
                    box[nx][ny][nz] = box[x][y][z] + 1
                    queue.append([nx, ny, nz])

    day = 0

    for mat in box:
        for row in mat:
            # 안 익은 토마토 발견시 -1
            if 0 in row:
                print(-1)
                exit()
            
            # 한 줄에서 최대값과 day를 비교해서 day를 최대값으로 변경
            day = max(day, max(row))

    # 익은 토마토는 1 이지만, 실제로는 0일차에 익은것을 나타내므로
    # day - 1이 실제로 토마토가 모두 익는데 걸리는 날짜를 나타냄
    print(day-1)