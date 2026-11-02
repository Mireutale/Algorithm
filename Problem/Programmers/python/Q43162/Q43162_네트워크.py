"""
컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers

네트워크의 개수를 return
"""
from collections import deque

def solution(n, computers):
    in_network = [False] * n
    answer = 0
    for i in range(n): # 모든 노드에 대해서 체크가 필요함
        if not in_network[i]: # 찾은 네트워크에 현재 노드가 없는 경우
            # 연결된 모든 노드를 찾아서 하나의 네트워크로 만들어야함
            answer += 1
            in_network[i] = True
            q = deque(
                node
                for node, connect in enumerate(computers[i]) 
                if connect and not in_network[node]
            )
            while q:
                next_node = q.popleft()
                in_network[next_node] = True
                q.extend(
                    node
                    for node, connect in enumerate(computers[next_node]) 
                    if connect and not in_network[node]
                )
    return answer

# 최적화 풀이
from collections import deque

def solution(n, computers):
    visited = [False] * n
    answer = 0
    for start in range(n):
        if visited[start]: # 이미 방문한 노드는 넘어가기
            continue

        # 새로운 네트워크 발견
        answer += 1
        visited[start] = True
        q = deque([start]) # 시작점부터 q에 넣기

        while q: # 방문처리
            current = q.popleft()
            for node, connected in enumerate(computers[current]):
                if connected and not visited[node]:
                    visited[node] = True
                    q.append(node)

    return answer