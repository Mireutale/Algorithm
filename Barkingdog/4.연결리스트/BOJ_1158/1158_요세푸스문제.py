"""
* Barkingdog\0x04 연결리스트\BOJ_1158\1158_요세푸스문제.py
* Author : mireutale
"""

import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

"""
[설계]

collections 라이브러리의 deque 사용
deque는 double-ended queue의 약자로, 양방향 삽입 삭제가 가능한 데이터를 의미
내부적으로는 링크드 리스트의 형태를 사용하고 있음.

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 순서대로 K번째 사람을 제거
원에서 사람들이 제거되는 순서를 출력
"""

if __name__ == "__main__":
    N, K = map(int, input().split())
    link_list = deque(i + 1 for i in range(N)) 
    Josephus = []
    while(len(link_list) > 0):
        link_list.rotate(-K)
        Josephus.append(link_list.pop())
    print("<" + ", ".join(str(num) for num in Josephus) + ">")