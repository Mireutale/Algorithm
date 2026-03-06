# Barkingdog/17.그리디/BOJ_11501/11501_주식.py

import sys
sys.setrecursionlimit(200000)
input = lambda: sys.stdin.readline().rstrip()

def is_cycle(current, prev, graph, visited):
    # 현재의 노드 방문 처리
    visited[current] = True

    for neighbor in graph[current]:
        # 양방향이므로, 부모는 무시
        if neighbor == prev:
            continue
        # 사이클 발생
        if visited[neighbor]:
            return True
        # 자식에서 사이클 발생
        if is_cycle(neighbor, current, graph, visited):
            return True
    
    return False

if __name__ == "__main__":
    cnt = 0
    while True:
        cnt += 1
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        
        # 간선을 모아 그래프 생성
        graph = [[] for _ in range(n+1)]
        for _ in range(m):
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)

        # 그래프에서 트리 찾기
        visited = [False] * (n+1)
        tree_cnt = 0

        for i in range(1, n+1):
            if not visited[i]:
                if not is_cycle(i, 0, graph, visited):
                    tree_cnt += 1

        print(f"Case {cnt}: ", end ="")
        if tree_cnt == 0:
            print("No trees.")
        elif tree_cnt == 1:
            print("There is one tree.")
        else:
            print(f"A forest of {tree_cnt} trees.")