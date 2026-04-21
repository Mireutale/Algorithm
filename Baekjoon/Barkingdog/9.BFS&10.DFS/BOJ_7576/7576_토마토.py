# Barkingdog/9.BFS&10.DFS/BOJ_7576/7576_토마토.py

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

"""
[설계]
가로 칸의 수 M, 세로 칸의 수 N (2 ~ M, N ~ 1,000)

상자안에 익은 토마토는 1, 익지 않은 토마토는 0, 토마토가 들어있지 않은 칸은 -1로 나타낸다

하루가 지나면 익은 토마토들의 인접한 곳에 있는 익지 않은 토마토 들은 익게 된다.
며칠이 지나면 모든 토마토가 익게 되는지 알고 싶음

출력 최소 날짜 or 불가능한 경우 -1을 출력

전체 box의 값을 확인해서 익은 토마토를 전부 queue에 day와 함께 입력
"""
if __name__ == "__main__":
    m, n = map(int, input().split())
    box = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    queue = deque()
    direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    day = 0
    # box를 순회하며 값이 1인 위치를 queue에 추가
    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                queue.append((i, j, day))  # (x, y, day) 형태로 추가
                visited[i][j] = True  # 방문 처리
                """
! 오류가 발생한 코드 부분 -> 뭔가 로직적인 오류가..
! 그냥 bfs를 모두 돌고도 안 익은 토마토가 남아있는것을 확인하는게 더 좋은거 같다.
            # 안 익은 토마토 중
            if box[i][j] == 0:
                impossible = True
                # 상하좌우 확인
                for dx, dy in direction:
                    x, y = i + dx, j + dy
                    # 상하좌우 중, -1이 아닌 값이 있다면 가능
                    if 0 <= x < n and 0 <= y < m:
                        if box[x][y] != -1:
                            impossible = False
                            break
                ! 여기 부분이 애매함
                ! 내부 작동 코드와 뭔가 다른게 있는거 같음
                if impossible:
                    print(-1)
                    exit()

    if not queue:
        print(-1)
        exit()
    """
    # 익은 토마토 기준 bfs
    while queue:
        x, y, day = queue.popleft()  # 현재 위치와 날짜를 가져옴
        for dx, dy in direction:
            nx, ny = x + dx, y + dy  # 새로운 위치 계산
            if 0 <= nx < n and 0 <= ny < m:  # 범위 내에 있는지 확인
                if box[nx][ny] == 0 and not visited[nx][ny]:  # 익지 않은 토마토이고 방문하지 않은 경우
                    box[nx][ny] = 1  # 토마토를 익힘
                    visited[nx][ny] = True  # 방문 처리
                    queue.append((nx, ny, day + 1))  # 새로운 위치와 날짜를 큐에 추가

    # 모든 토마토가 익었는지 확인
    for row in box:
        if 0 in row:  # 익지 않은 토마토가 남아있으면
            print(-1)
            exit()

    # 모든 토마토가 익었다면 마지막 날짜 출력
    print(day)
