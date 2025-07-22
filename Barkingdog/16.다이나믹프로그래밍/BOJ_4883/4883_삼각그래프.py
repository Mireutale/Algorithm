"""
* CodingTest/Barkingdog/16.다이나믹프로그래밍/BOJ_4883/4883_삼각그래프.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    test_case_count = 0
    while True:
        test_case_count += 1
        N = int(input())
        if N == 0:
            break
        graph = [list(map(int, input().split())) for _ in range(N)]
        graph[1][0] += graph[0][1]
        graph[1][1] += min(graph[0][1], graph[0][1] + graph[0][2], graph[1][0])
        graph[1][2] += min(graph[0][1], graph[0][1] + graph[0][2], graph[1][1])
        #중간
        for i in range(2,N):
            graph[i][0] += min(graph[i-1][0], graph[i-1][1])
            graph[i][1] += min(graph[i-1][0], graph[i-1][1], graph[i-1][2], graph[i][0])
            graph[i][2] += min(graph[i-1][1], graph[i-1][2], graph[i][1])
        print(f"{test_case_count}. {graph[N-1][1]}")

"""
commit msg
Solved / Working

- Body

Date : [25/06/01] 
"""