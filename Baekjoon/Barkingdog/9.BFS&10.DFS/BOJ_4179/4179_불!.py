# Barkingdog/9.BFS&10.DFS/BOJ_4179/4179_불!.py

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque
"""
[설계]

"#" : 벽
"." : 지나갈 수 있는 공간
"J" : 초기 위치
"F" : 불이 난 공간
"""

if __name__ == "__main__":
    r, c = map(int, input().split())
    maze = list(list(input()) for _ in range(r))
    queue = deque()
    for i in range(r):
        for j in range(c):
            if maze[i][j] == "J":
                queue.appendleft([i, j, 0])
            elif maze[i][j] == "F":
                queue.append([i, j, 0])

    direction = ((-1, 0), (1, 0), (0, -1), (0, 1))

    while queue:
        # print(queue)
        y, x, time = queue.popleft()
        if maze[y][x] == "J":
            # 미로 끝 탈출
            if y == 0 or x == 0 or x == c-1 or y == r-1:
                print(time + 1)
                exit()
        time += 1
        for i in range(4):
            nx, ny = x + direction[i][0], y + direction[i][1]
            if 0 <= nx < c and 0 <= ny < r and not maze[ny][nx] == "#":      
                # 사람
                if maze[y][x] == "J":
                    if maze[ny][nx] == ".":
                        # 미로 안, 빈 공간만 이동가능
                        queue.append([ny, nx, time])
                        maze[ny][nx] = maze[y][x]
                # 불
                elif maze[y][x] == "F":
                    if not maze[ny][nx] == "F":
                        # 불, 벽 제외 이동가능
                        queue.append([ny, nx, time])
                        maze[ny][nx] = maze[y][x]

    print("IMPOSSIBLE")
