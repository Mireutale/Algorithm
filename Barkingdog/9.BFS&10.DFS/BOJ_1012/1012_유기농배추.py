"""
* CodingTest/Barkingdog/9.BFS&10.DFS/BOJ_1012/1012_유기농배추.py
* Author : mireutale
"""

import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

"""
[설계]
1은 배추가 있는 땅, 0은 배추가 없는 땅

배추흰지렁이 한마리는 인접한 다른 배추로 이동가능(상하좌우)하고
이 배추들도 안전

첫 줄 테스트 케이스의 개수 T
이후 테스트케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로M, 세로N
배추 위치의 개수 K가 주어짐.
이후 K줄에 걸쳐 배추의 위치가 주어짐.

최소한의 배추흰지렁이의 수를 출력
"""

def bfs(x, y, graph, M, N):
    # 현재 위치의 배추를 방문 처리
    graph[y][x] = 0
    queue = deque([(x, y)])
    
    # 상하좌우 이동을 위한 방향 벡터
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    while queue:
        x, y = queue.popleft()
        # 상하좌우 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            # 범위 내에 있고, 배추가 있는 경우
            if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 1:
                graph[ny][nx] = 0  # 방문 처리
                queue.append((nx, ny))

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        M, N, K = map(int, input().split())
        graph = [[0] * M for _ in range(N)]
        
        # 배추 위치 입력
        for _ in range(K):
            x, y = map(int, input().split())
            graph[y][x] = 1
        
        # 지렁이 수 계산
        worm_count = 0
        for y in range(N):
            for x in range(M):
                if graph[y][x] == 1:  # 배추가 있는 경우
                    bfs(x, y, graph, M, N)
                    worm_count += 1
        
        print(worm_count)

