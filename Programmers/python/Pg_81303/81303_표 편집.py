# PG 81303 표 편집

import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

class Linked_Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def solution(n, k, cmd):
    # 링크드 리스트 초기화
    nodes = [Linked_Node(1) for _ in range(n)]
    for i in range(n - 1):
        nodes[i].next = nodes[i + 1]
        nodes[i + 1].prev = nodes[i]
    
    cursor = nodes[k]
    delete = deque()
    
    for command in cmd:
        # U or D cmd
        if len(command) > 1:
            command, move = command.split()
            move = int(move)
        
        if command == "U":
            for _ in range(move):
                cursor = cursor.prev

        if command == "D":
            for _ in range(move):
                cursor = cursor.next

        # 행 삭제
        if command == "C":
            delete.append(cursor)
            # 삭제 상태 표시
            cursor.data = 0
            # 커서의 이전 노드는 커서의 다음 노드를 가리키도록
            if cursor.prev:
                cursor.prev.next = cursor.next
            # 커서의 다음 노드는 커서의 이전 노드를 가리키도록 설정
            if cursor.next:
                cursor.next.prev = cursor.prev
            # cursor.next가 없으면 마지막 노드이므로, 이전 노드로 커서 이동
            if not cursor.next:
                cursor = cursor.prev
            else:
                cursor = cursor.next 

        if command == "Z":
            node = delete.pop()
            # 노드 복구
            node.data = 1
            if node.prev:
                node.prev.next = node
            if node.next:
                node.next.prev = node

    answer = ''.join('O' if node.data == 1 else 'X' for node in nodes)
    return answer

if __name__ == "__main__":
    n = int(input())
    k = int(input())
    cmd = input().strip('[]').replace('"', '').split(', ')
    print(solution(n, k, cmd))