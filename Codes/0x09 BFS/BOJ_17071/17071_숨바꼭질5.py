"""
* Codes/0x09 BFS/BOJ_2206/2206_벽부수고이동하기.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def bfs(k, queue):
    next_queue = deque()
    time = 0
    destination = k
    while True:
        destination += time
        if destination > 500000:
            return print(-1)
        while queue:
            x = queue.popleft()
            if visited[destination] != -1:
                # * visited[destination]이 0이 아닌 경우
                if (time - visited[destination]) % 2 == 0:
                    return print(time)
            else:
                for nx in (x*2, x+1, x-1):
                    if 0 <= nx <= 500000 and visited[nx] == -1:
                        next_queue.append(nx)
                        visited[nx] = time + 1
        time += 1
        next_queue, queue = queue, next_queue



if __name__ == "__main__":
    n, k = map(int, input().split())
    # * 방문한 시간을 저장
    visited = [-1] * 500001
    queue = deque()
    queue.append(n)
    visited[n] = 0
    bfs(k, queue)

# commit msg
# --- 문제풀이_mireutale[25/ / ]