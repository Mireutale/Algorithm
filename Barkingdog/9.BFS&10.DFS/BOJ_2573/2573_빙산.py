# Barkingdog/9.BFS&10.DFS/BOJ_2573/2573_빙산.py

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def count_iceberg(y, x):
    queue = deque()
    queue.append([y, x])
    visitied[y][x] = True
    while queue:
        y, x = queue.popleft()
        iceberg.append([y, x]) # * 빙산의 위치를 따로 저장
        for i in range(4):
            ny, nx = y + direction[i][0], x + direction[i][1]
            if 0 <= ny < n and 0 <= nx < m and not visitied[ny][nx]:
                # ? 상하좌우에 위치 & 아직 지나지 않고 빙산의 일부인 경우
                if given_map[ny][nx] != 0:
                    queue.append([ny, nx])
                    visitied[ny][nx] = True




def after_year():
    melt_iceberg = deque()
    while iceberg:
        y, x = iceberg.popleft()
        count_water = 0
        for i in range(4):
            ny, nx = y + direction[i][0], x + direction[i][1]
            # ? 범위 안에 있고
            if 0 <= ny < n and 0 <= nx < m:
                # ? 물인 경우의 수를 체크
                if given_map[ny][nx] == 0:
                    count_water += 1
        melt_iceberg.append([y, x, count_water])
    
    # 녹는걸 한번에 적용
    while melt_iceberg:
        y, x, count_water = melt_iceberg.popleft()
        given_map[y][x] -= count_water
        if given_map[y][x] < 0:
            given_map[y][x] = 0

if __name__ == "__main__":
    n, m = map(int, input().split())
    given_map = [list(map(int, input().split())) for _ in range(n)]
    # * 지나간 해
    year = 0
    # * 빙산의 위치를 iceberg에 저장
    iceberg = deque()
    direction = ((-1, 0), (1, 0), (0, -1), (0, 1))
    while True:
        count = 0
        visitied = [[False]*m for _ in range(n)]
        # * 모든 빙산의 개수 구하기
        for i in range(n):
            for j in range(m):
                if given_map[i][j] != 0 and not visitied[i][j]:
                    # 빙산이 존재하는 경우
                    count += 1
                    count_iceberg(i, j)
        if len(iceberg) == 1:
            print(0)
            exit()
        
        if count >= 2:
            print(year)
            exit()
        elif count == 1:
            after_year()
            year += 1
        elif count == 0:
            print(0)
            exit()
