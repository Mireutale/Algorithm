# PG 42840 모의고사 문제

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def solution(n, edge):
    # graph 생성
    graph = [[] for _ in range(n+1)]
    
    # edge의 양끝 노드에 연결된 노드 입력
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    # 거리 설정
    distance = [-1] * (n+1)
    # 기준 노드가 1 이므로, 1번의 거리 0으로 설정
    distance[1] = 0
    
    q = deque([1])
    
    while q:
        # 현재 위치 선택
        current = q.popleft()
        
        # 현재 노드와 연결되어 있는 다른 노드들
        for next in graph[current]:
            # 다른 노드까지의 거리가 -1로 한번도 도착한 적 없다면? > 처음 만나는 노드
            if distance[next] == -1:
                # 현재 노드의 거리 + 1을 다음 노드로 선택
                distance[next] = distance[current] + 1
                q.append(next)
                
    answer = distance.count(max(distance))
    return answer

if __name__ == "__main__":
    n = 6
    edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    print(solution(n, edge))