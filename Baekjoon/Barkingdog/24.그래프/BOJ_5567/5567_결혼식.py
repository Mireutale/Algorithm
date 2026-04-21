# Barkingdog/24.그래프/BOJ_5567/5567_결혼식.py

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

if __name__ == "__main__":
    n = int(input())
    edge = int(input())
    edges = []
    for _ in range(edge):
        edges.append(list(map(int, input().split())))
    
    graph = [[] for _ in range(n+1)]
    for i in range(edge):
        x, y = edges[i]
        graph[x].append(y)
        graph[y].append(x)
    
    cnt = 0
    visited = [False] * (n+1)
    visited[1] = True
    queue = deque([(1, 0)])
    while queue:
        now, depth = queue.popleft()
        if depth < 2:
            for connect in graph[now]:
                if visited[connect] != True:
                    queue.append((connect, depth+1))
                    visited[connect] = True
    
    print(sum(visited) - 1)
