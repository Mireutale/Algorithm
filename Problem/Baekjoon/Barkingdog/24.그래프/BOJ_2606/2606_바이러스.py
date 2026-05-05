# Barkingdog/24.그래프/BOJ_2606/2606_바이러스.py

import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    nodes = int(input())
    n = int(input())
    edges = []
    for _ in range(n):
        edges.append(list(map(int, input().split())))

    graph = [[] for _ in range(nodes+1)]
    for i in range(n):
        x, y = edges[i]
        graph[x].append(y)
        graph[y].append(x)
    
    visited = [False] * (nodes + 1)
    visited[1] = True
    deck = deque([1])
    # count = 0
    while deck:
        next = deck.popleft()
        for connected in graph[next]:
            if visited[connected] != True:
                deck.append(connected)
                # count += 1
                visited[connected] = True
    
    # print(count)
    print(sum(visited) - 1)