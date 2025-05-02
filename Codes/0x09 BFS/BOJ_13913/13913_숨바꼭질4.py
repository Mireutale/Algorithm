"""
* Codes/0x09 BFS/BOJ_2206/2206_벽부수고이동하기.py
* Author : mireutale

* input을 빠르게 받기 위한 sys 라이브러리 사용
* sys.stdin.readline()을 사용해서 input보다 더 빠르게 값을 입력받음
* rstrip()을 사용해서 마지막 개행문자 '\n'을 입력받지 않도록 설정
* lambda함수를 사용해서 input을 sys.stdin.readline().rstrip()으로 대체

TODO 
[설계]

수빈이의 위치 N, 동생의 위치 K, (0 ~ N, K ~ 100,000)
수빈이가 걷는다면 1초 후 -1 or +1
수빈이가 순간이동을 하는 경우 1초 후 2배
동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후, 이동경로를 출력하시오
"""

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

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
    route_recovery = [-1] * 100001
    route_recovery[n] = 0
    while queue:
        x = queue.popleft()
        if x == k:
            # * 걸린 시간 출력
            print(visited[x] - 1)
            route = []
            while route_recovery[k] != -1:
                route.append(k)
                t = route_recovery[k]
                # * 복구 완료 후, 모두 -1로 초기화
                route_recovery[k] = -1
                if t == 0:
                    break
                else:
                    k = t
            # * 이동경로 출력
            print(*route[::-1])
            exit()
        for nx in (x*2, x+1, x-1):
            # * 범위 내 & 방문하지 않은 점(visited[nx] == 0)인 경우에만 이동
            if 0 <= nx <= 100000 and not visited[nx]:
                visited[nx] = visited[x] + 1
                # * nx로 이동하기전 위치인 x를 저장
                route_recovery[nx] = x
                queue.append(nx)


"""
5 17
나머지 route_recovery == -1
visited[5] = 1, route_recovery[5] = 0
visited[10] = 2, route_recovery[10] = 5
visited[9] = 3, route_recovery[9] = 10
visited[18] = 4, route_recovery[18] = 9
visited[17] = 5, route_recovery[17] = 18

0 0

visited[0] = 1, route_recovery[0] = 0

0 4
visited[0] = 1, route_recovery[0] = 0
visited[1] = 2, route_recovery[1] = 0
visited[2] = 3, route_recovery[2] = 1
visited[4] = 4, route_recovery[4] = 2
ans [4, 2, 1]
"""
# commit msg
# --- 문제풀이_mireutale[25/ / ]