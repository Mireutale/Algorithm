"""
* Barkingdog\0x09 BFS\BOJ_11967\11967_불켜기.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque, defaultdict

def light_room(switch_dict):
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    ans = 1
    
    while queue:
        x, y = queue.popleft()
        
        # 현재 위치에서 스위치로 불을 켤 수 있는 방 확인
        if (x, y) in switch_dict:
            for c, d in switch_dict[(x, y)]:
                if not light[c][d]:  # 불이 꺼져있는 방이면
                    light[c][d] = True
                    ans += 1
                    # 새로 불을 켠 방의 주변을 확인
                    for dx, dy in direction:
                        nx, ny = c + dx, d + dy
                        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny]:
                            # 이미 방문한 방 근처에 불을 켰다면 queue에 추가
                            if not visited[c][d]:
                                visited[c][d] = True
                                queue.append((c, d))
        
        # 현재 위치에서 이동할 수 있는 방 확인
        for dx, dy in direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and light[nx][ny]:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    
    return ans

if __name__ == "__main__":
    n, m = map(int, input().split())
    # 방문 여부 확인
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True
    # 불 켜진 방
    light = [[False] * n for _ in range(n)]
    light[0][0] = True
    # 스위치 위치를 딕셔너리로 저장, 딕셔너리의 기본값은 빈 리스트
    switch_dict = defaultdict(list)
    for i in range(m):
        x, y, a, b = map(int, input().split())
        switch_dict[(x-1, y-1)].append((a-1, b-1))
    queue = deque([(0, 0)])
    print(light_room(switch_dict))