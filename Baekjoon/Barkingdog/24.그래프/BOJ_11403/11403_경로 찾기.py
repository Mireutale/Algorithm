# Barkingdog/24.그래프/BOJ_11403/11403_경로 찾기.py

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input())
    edges = [list(map(int, input().split())) for _ in range(n)]
    # ? i -> k -> j 형태로 이동가능한 모든 경로를 체크하자.
    for k in range(n): # 중간 경유지
        for i in range(n): # 시작 노드
            for j in range(n): # 도착 노드
                if edges[i][k] == 1 and edges[k][j] == 1:
                    edges[i][j] = 1
    
    for row in edges:
        print(*row)