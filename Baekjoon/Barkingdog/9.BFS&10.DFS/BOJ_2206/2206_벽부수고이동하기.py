# Barkingdog/9.BFS&10.DFS/BOJ_2206/2206_벽부수고이동하기.py

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def bfs(n, m):
    direction = ((-1, 0), (1, 0), (0, -1), (0, 1))

    while queue:
        y, x, move_count, break_wall = queue.popleft()
        if y == n-1 and x == m-1:
            return move_count
        if break_wall: # * 벽을 깬 상태인 경우
            for i in range(4):
                ny, nx = y + direction[i][0], x + direction[i][1]
                if 0 <= ny < n and 0 <= nx < m:
                    # * 이미 벽을 깬 상태이므로, 벽이 아닌 경우만 이동 가능
                    if given_map[ny][nx] == "0":
                        # * 해당 위치를 벽을 깬 상태로 방문한 적이 없는 경우
                        if not break_visited[ny][nx]:
                            queue.append([ny, nx, move_count+1, break_wall])
                            break_visited[ny][nx] = True
        else: # * 벽을 깨지 않은 상태인 경우
            for i in range(4):
                ny, nx = y + direction[i][0], x + direction[i][1]
                if 0 <= ny < n and 0 <= nx < m:
                    # * 벽을 깨지 않은 상태이므로, 벽을 깨고 이동 가능
                    if given_map[ny][nx] == "1":
                        # * 해당 위치가 벽을 깬 상태로 이동한 적이 없는 경우
                        if not break_visited[ny][nx]:
                            queue.append([ny, nx, move_count+1, not break_wall])
                            break_visited[ny][nx] = True
                    # * 그냥 이동 가능한 경우
                    else:
                        # * 벽을 깨지 않은 상태로 이동한 적 없는 경우
                        if not not_break_visited[ny][nx]:
                            queue.append([ny, nx, move_count+1, break_wall])
                            not_break_visited[ny][nx] = True
    return -1

if __name__ == "__main__":
    n, m = map(int, input().split())
    given_map = [list(input()) for _ in range(n)]
    # * 벽을 깨지 않은 상태에서 방문
    not_break_visited = [[False]*m for _ in range(n)]
    # * 벽을 깬 상태에서 방문
    break_visited = [[False]*m for _ in range(n)]
    # * 시작 위치[y, x], 이동한 거리, 부신 벽의 개수
    queue = deque([(0, 0, 1, False)])
    not_break_visited[0][0] = True
    print(bfs(n, m))
