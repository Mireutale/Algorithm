"""
* Barkingdog\0x09 BFS\BOJ_2583\2583_영역구하기.py
* Author : mireutale
"""
import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

"""
[설계]
M*N (자연수 M, N <= 100)

값을 받고, board안에 box와 겹치는 값을 전부 True로 변경
이후, 이중 for문을 돌면서 False인 값에 대해서 bfs를 수행
False인 값을 발견하면 분할된 부분 1개를 추가
bfs를 수행하면서 분할된 부분의 넓이를 구하고, 분할된 부분의 영역을 True로 변경
"""

def bfs(board, y, x):
    queue = deque()
    queue.append([x, y])
    board[x][y] = True
    area = 1
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위내에 있는지 확인
            if 0 <= nx < M and 0 <= ny < N:
                # box가 아니고, 아직 지나지 않은 상황인 경우
                if board[nx][ny] == False:
                    area += 1
                    queue.append([nx, ny])
                    board[nx][ny] = True
    
    return area

if __name__ == "__main__":
    M, N, K = map(int, input().split())
    board = [[False] * N for _ in range(M)]
    for _ in range(K):
        x1, y1, x2, y2 = map(int, input().split())
        for j in range(x1, x2):
            for i in range(y1, y2):
                board[i][j] = True
    
    count = 0
    area_s = deque()

    for i in range(N):
        for j in range(M):
            if board[j][i] == False:
                count += 1
                area_s.append(bfs(board, i, j))
    print(count)
    area_s = list(sorted(area_s))
    print(*area_s)