"""
* CodingTest/Barkingdog/9.BFS&10.DFS/BOJ_1926/1926_그림.py
* Author : mireutale
"""
import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
"""
[설계]
세로 n, 가로 m (1 ≤ n ≤ 500, 1 ≤ m ≤ 500)
0은 빈칸, 1은 그림
그림의 개수와 가장 넓은 그림의 넓이를 출력
가로, 세로로 연결된 것은 하나의 그림
대각선은 연결되지 않은 그림
"""

# 시작점을 x, y로 받아서 주변의 값을 확인하는 함수
def bfs(x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    area = 1
    
    # 상하좌우 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 범위 체크
            if 0 <= nx < n and 0 <= ny < m:
                # 그림이고 방문하지 않았다면
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    area += 1
    # 그림의 넓이 반환
    return area

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    # 방문 여부 확인 -> 방문하면 True, 방문하지 않으면 False
    visited = [[False] * m for _ in range(n)]
    count = 0
    max_area = 0
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                count += 1
                area = bfs(i, j, visited)
                max_area = max(max_area, area)

    print(count)
    print(max_area) 