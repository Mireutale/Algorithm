# Barkingdog/9.BFS&10.DFS/BOJ_13913/13913_숨바꼭질4.py

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def time_and_move(x, k):
    # * 걸린 시간 출력
    print(visited[x] - 1)
    route = [k]
    # * 걸린 시간 만큼의 경로를 찾기
    for _ in range(visited[x]-1):
        route.append(route_recovery[k])
        k = route_recovery[k]
    print(*route[::-1])

def bfs(k):
    while queue:
        x = queue.popleft()
        if x == k:
            time_and_move(x, k)
        for nx in (x*2, x+1, x-1):
            # * 범위 내 & 방문하지 않은 점(visited[nx] == 0)인 경우에만 이동
            if 0 <= nx <= 100000 and not visited[nx]:
                visited[nx] = visited[x] + 1
                # * nx로 이동하기전 위치인 x를 저장
                route_recovery[nx] = x
                queue.append(nx)

if __name__ == "__main__":
    n, k = map(int, input().split())
    queue = deque()
    queue.append(n)
    # ! queue.append([n, 0, [n]]) -> 모든 route를 저장하는 것은 메모리 낭비!
    # ? 복구 번호를 쫓아가면서 결과를 호출하도록 하자
    # * 방문 순서를 저장하는 visitied
    visited = [0] * 100001
    visited[n] = 1
    # * 방문 경로를 위한 리스트
    # ! 0도 방문 가능한 위치이므로 -1로 초기화 시켜놓아야 함
    route_recovery = [-1] * 100001
    bfs(k)
