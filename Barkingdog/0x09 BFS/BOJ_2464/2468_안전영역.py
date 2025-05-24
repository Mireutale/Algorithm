"""
* Barkingdog\0x09 BFS\BOJ_2468\2468_안전영역.py
* Author : mireutale
"""
import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

"""
[설계]
행과 열의 크기가 각각 N인 2차원 배열에 해당 지점의 
높이를 표시하는 자연수 형태로 높이 정보(h)가 주어짐

물에 잠기지 않는 안전한 영역 = 잠기지 않는 지점이 상하좌우로
인접해 있으며 그 크기가 최대인 영역을 말한다. 
"""

def search_area(rand, rain_h, N, x, y, visited):
    queue = deque([(x, y)])
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 내이고 아직 방문하지 않은 지역인 경우
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                # 물에 잠기지 않는 지역
                if rain_h < rand[nx][ny]:
                    # 물에 잠기지 않는 지역을 queue에 추가
                    queue.append([nx, ny])
                    visited[nx][ny] = True


if __name__ == "__main__":
    N = int(input()) # (2 ~ N ~ 100)
    rand = [list(map(int, input().split())) for _ in range(N)] # (1 ~ h~ 100)
    max_count = 0
    # ! max_h = max(max(rand))
    # * max를 2차원 리스트에서 사용하는 경우 리스트간의 크기를 비교하게 된다.
    # * 즉, 첫번째 원소끼리 비교해서 더 큰 리스트가 선택되는 것, 이를 해결하기 위해서 각 행을 따로 호출해서 max를 사용한다.
    max_h = max(max(row) for row in rand)
    # 0부터 가장 높은 높이 -1까지
    # ? 아무 지역도 물에 잠기지 않을 수 있다 -> 물의 높이 0
    # ? 가장 높은 높이와 물의 높이가 같으면? -> 물에 잠기지 않는 영역 없음
    for i in range(max_h): 
        visited = [[False]*N for _ in range(N)]
        count = 0
        for j in range(N):
            for k in range(N):
                if not visited[j][k] and rand[j][k] > i:
                    count += 1
                    search_area(rand, i, N, j, k, visited)
        max_count = max(max_count, count)
    print(max_count)