# Barkingdog/9.BFS&10.DFS/BOJ_2178/2178_미로탐색.py

import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

"""
[설계]
N * M 크기의 배열 -> 미로
1은 이동할 수 있는 칸, 0은 이동할 수 없는 칸

(1, 1)에서 출발하여, (M, N)위치로 이동할 때, 지나야 하는 최소의 칸 수를 구하기

bfs활용
이동한 위치 visited, 설정 (m, n)에 도착한 경우에 이동 거리를 distance로 두고 min값을 구하기.
"""
def bfs(x, y, mage):
    # 이동한 위치인지 아닌지 파악하기 위한 배열
    # boolean 배열을 활용하는 것이, set을 활용해서 방문한 점을 추가하는 것보다 더 빠르다.
    visited = [[False] * M for _ in range(N)]
    # 이동한 거리를 파악하기 위한 배열
    distance = [[0] * M for _ in range(N)]
    # 시작 지점 방문 처리 및 이동거리 1로 설정
    visited[x][y] = True
    distance[x][y] = 1

    # 상, 하, 좌, 우 이동을 위한 방향 벡터
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    
    queue = deque([(x, y)])
    while queue:
        current_x, current_y = queue.popleft()
        
        # 목적지에 도달한 경우 즉시 반환
        if current_x == N-1 and current_y == M-1:
            return distance[current_x][current_y]
        
        # 상하좌우 이동
        for dx, dy in directions:
            nx, ny = current_x + dx, current_y + dy
            
            # 범위 체크 및 이동 가능 여부 확인
            if 0 <= nx < N and 0 <= ny < M and mage[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                distance[nx][ny] = distance[current_x][current_y] + 1
                queue.append((nx, ny))
    
    return distance[N-1][M-1]  # 도달할 수 없는 경우

if __name__ == "__main__":
    N, M = map(int, input().split())
    mage = list([] for _ in range(N))
    for i in range(N):
        input_line = input()
        for data in input_line:
            mage[i].append(int(data))
    print(bfs(0, 0, mage))
