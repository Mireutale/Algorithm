# Barkingdog/25.트리/BOJ_15681/15681_트리와 쿼리.py

import sys
input = lambda: sys.stdin.readline().rstrip()
# ! 서브쿼리를 세는데, 많은 재귀가 일어날 수 있으므로, 제한값을 늘림
sys.setrecursionlimit(200000)

# ? 루트노드를 parent_node로 두면, 
def count_subtree_nodes(parent_node):
    size[parent_node] = 1 # 자기 자신 포함
    for child in graph[parent_node]:
        if size[child] == 0: # 방문하지 않은 자식 노드
            count_subtree_nodes(child) # 자식노드의 서브 쿼리의 크기를 구함
            size[parent_node] += size[child] # 자식의 크기를 더함

if __name__ == "__main__":
    n, r, q = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(n-1):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    size = [0] * (n + 1)
    count_subtree_nodes(r)
    for _ in range(q):
        parent = int(input())
        # ? 서브 트리의 정점 = 서브트리를 이루는 모든 노드의 개수
        print(size[parent])