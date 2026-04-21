# Barkingdog/17.그리디/BOJ_11399/11399_ATM.py

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def find_legnth(start, end):
    queue = deque([(start, 0)])
    visitied = [False] * (n+1)
    visitied[start] = True
    while queue:
        curr, length = queue.popleft()
        if end == curr:
            return length
        
        for next, weight in graph[curr]:
            if visitied[next] != True:
                queue.append((next, length + weight))
                visitied[next] = True

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        x, y, far = list(map(int, input().split()))
        graph[x].append((y, far))
        graph[y].append((x, far))
    for _ in range(m):
        x, y = map(int, input().split())
        print(find_legnth(x, y))
