"""
* Codes\0x09 BFS\BOJ_2146\2146_다리만들기.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def bfs(y, x, continent_num):
    queue = deque([[y, x]])
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + direction[i][0], x + direction[i][1]
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                # 육지인 경우
                if world_map[ny][nx] == 1:
                    visited[ny][nx] = True
                    queue.append([ny, nx])
                # 바다인 경우
                else:
                    if [y, x] not in continent_boundary[continent_num]:
                        continent_boundary[continent_num].append([y, x])

if __name__ == "__main__":
    n = int(input())
    world_map = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    # 대륙 및 바다와 만나는 경계선 찾기
    continent = 0
    continent_boundary = {}  # 대륙별 경계선을 저장할 딕셔너리
    for i in range(n):
        for j in range(n):
            if world_map[i][j] == 1 and not visited[i][j]:
                continent += 1
                continent_boundary[continent] = []  # 새로운 대륙의 경계선 리스트 초기화
                bfs(i, j, continent)

    min_distance = float('inf')
    # 서로 다른 대륙의 경계선들 사이의 최소 거리 계산
    for i in range(1, continent + 1):
        for j in range(i + 1, continent + 1):
            for point1 in continent_boundary[i]:
                for point2 in continent_boundary[j]:
                    min_distance = min(min_distance, abs(point1[0] - point2[0]) + abs(point1[1] - point2[1]) - 1)
    
    print(min_distance)