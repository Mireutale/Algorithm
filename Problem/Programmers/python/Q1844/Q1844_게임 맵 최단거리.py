"""
상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 최솟값을 return
단, 상대 팀 진영에 도착할 수 없을 때는 -1을 return
캐릭터는 처음에 1, 1에 위치하고, 상대방 진영은 게임 맵의 우측 하단인 n, m에 위치함
"""
from collections import deque

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    # 처음 시작은 1,1에서 이동한 칸의 수 1
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    q = deque([[0, 0, 1]])
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # 반복해서 다음 단계로 이동
    while q:
        x, y, room = q.popleft()
        if x == n-1 and y == m-1:
            return room
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            # 맵 범위 내에 있음
            if 0 <= nx < n and 0 <= ny < m:
                # 방문하지 않고, 벽이 없어야만 이동 가능
                if not visited[nx][ny] and maps[nx][ny] == 1: 
                    visited[nx][ny] = True
                    q.append([nx, ny, room+1])

    # 벽으로 막혀있는 경우
    return -1