"""
* Barkingdog\0x09 BFS\BOJ_13549\13549_숨바꼭질3.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque
"""
[설계]
수빈이는 동생과 숨바꼭질
수빈이의 현재 위치는 점 N, 동생은 점 K에 위치(0 ~ N, K ~ 100,000)
수빈이는 걷거나 순간이동 가능
수빈이의 위치가 X일때 걷는다면 1초후에 X-1 또는 X+1로 이동
순간이동을 수행하면 0초 후에 2*X의 위치로 이동

동생을 찾는데 걸리는 시간
"""

if __name__ == "__main__":
    n, k = map(int, input().split())
    queue = deque()
    queue.append([n, 0])
    visited = [False] * 100001
    while queue:
        x, time = queue.popleft()
        if x == k:
            print(time)
            exit()
        else:
            if not visited[x]:
                visited[x] = True
                if not x*2 > 100000:
                    queue.append([x*2, time])
                time += 1
                # ! x-1을 먼저 queue에 넣어야 한다.
                # ? 이유는 bfs를 수행하면서 값을 찾아나갈때, 가장 먼저 해당 값에 도달하면 exit로 탈출을 수행하는데, -1의 경우를 먼저 수행한다면 *2는 시간의 변화를 주지 않기 때문에
                # ? -1 * 2^n의 형태로 정답을 찾을 수 있는 경우가 걷는것 보다 짧은 시간이 될 것이다.
                # * 그런데 여기서 문제 -> 순간이동의 경우도 2회가 지나야 하는데, 2회 후 걸어서 도착이 가능하다면?
                # +1을 먼저 넣게되면 걸어서 도착하는 것을 최단시간으로 볼 것이다. 그러나 순간이동을 수행 한 결과가 최단시간이기 때문에 -1을 먼저 넣어서 순간이동을 먼저 고려하는게 옳다.
                """
                Todo 잘못 계산하는 예시
                n = 4, k = 6
                4 -> 5 -> 6 time = 2
                4 -> 3 -> 6 time = 1
                실제 최단시간은 1이지만, +1을 먼저 queue에 넣는다면 4->5->6으로 도달하는 게 먼저 찾아짐!!
                """
                if not x-1 < 0:
                    queue.append([x-1, time])
                if not x+1 > 100000:
                    queue.append([x+1, time])