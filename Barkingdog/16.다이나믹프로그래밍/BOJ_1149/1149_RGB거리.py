"""
* CodingTest\Barkingdog\16.다이나믹프로그래밍\BOJ_1149\1149_RGB거리.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    for i in range(1, N):
        graph[i][0] += min(graph[i-1][1], graph[i-1][2]) # R
        graph[i][1] += min(graph[i-1][0], graph[i-1][2]) # G
        graph[i][2] += min(graph[i-1][0], graph[i-1][1]) # B
    print(min(graph[N-1]))