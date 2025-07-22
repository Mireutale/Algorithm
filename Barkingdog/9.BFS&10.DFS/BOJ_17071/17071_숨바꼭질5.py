"""
* CodingTest/Barkingdog/9.BFS&10.DFS/BOJ_17071/17071_숨바꼭질5.py
* Author : mireutale
"""
import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

# * 수빈이와 동생이 이동 가능한 최대 값, 최소값
MAX = 500000
MIN = 0

def bfs(n, k):
    # * 짝수, 홀수
    visited = [[False, False] for _ in range(MAX + 1)]
    queue = deque([n])
    # * t = 0인 경우 짝수 시간
    visited[n][0] = True

    time = 0
    while True:
        # * 시간에 따른 목적지를 계산
        destiantion = k + time * (time + 1) // 2
        if destiantion > MAX:
            return -1
        # * 만약 목적지가 2의 배수만큼 뺐을 때
        # ? 도달 가능한 경우(+1, -1을 수행하면 제자리)
        # ! 굳이 이전 상황에서 //2, -1, +1을 찾는게 더 오래걸림 및 오류 발생 가능성
        if visited[destiantion][time % 2]:
            return time

        # * 다음 queue를 생성
        next_queue = deque()
        while queue:
            x = queue.popleft()
            for nx in (x - 1, x + 1, x * 2):
                if MIN <= nx <= MAX and not visited[nx][(time + 1) % 2]:
                    visited[nx][(time + 1) % 2] = True
                    next_queue.append(nx)
        """
        학습, 대회 등 간결성이 우선: queue = next_queue
        성능, 최적화, 반복 구조 재사용 고려 시: queue, next_queue = next_queue, queue
        """
        next_queue, queue = queue, next_queue
        time += 1

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(bfs(n, k))