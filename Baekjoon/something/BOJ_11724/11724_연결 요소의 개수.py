"""
* CodingTest/Something/BOJ_11724/11724_연결 요소의 개수.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

if __name__ == "__main__":
    n, m = map(int, input().split())
    nodes = set(range(1, n+1))
    line = []
    for _ in range(m):
        line.append(list(map(int, input().split())))
    
    components = []
    connected = set()

    for u, v in line:
        connected.update([u, v])
        new_set = set([u, v])
        merged = []

        for comp in components:
            if u in comp or v in comp:
                new_set |= comp  # 기존의 요소와 병합
            else:
                merged.append(comp)

        merged.append(new_set)
        components = merged

    for solo in nodes - connected:
        components.append(set([solo]))
    
    print(len(components))