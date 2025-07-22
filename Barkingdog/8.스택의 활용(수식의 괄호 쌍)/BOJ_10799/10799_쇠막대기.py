"""
* CodingTest/Barkingdog/8.스택의 활용(수식의 괄호 쌍)/BOJ_10799/10799_쇠막대기.py
* Author : mireutale
"""

import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

"""
[설계]
쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있고
쇠막대기를 다른 쇠 막대기 위에 놓는 경우, 끝점은 겹치지 않도록 놓는다.
각 쇠막대기를 자르는 레이저는 적어도 하나 존해하고, 레이저는 어떤 쇠막대기의
양 끝점과도 겹치지 않는다.

레이저와 쇠 막대기의 배치는 괄호를 이용하여 표현
레이저는 여는 괄호와 닫는 괄호의 인접한 쌍'()'으로 표현된다.
모든 '( )'는 반드시 레이저를 표현한다.

쇠 막대기의 왼쪽끝은 ( 으로 오른쪽 끝은 )으로 표현된다.

잘려진 쇠막대기 조각의 총 개수를 구하시오.

! 시간초과 -> deck을 사용해서 count를 늘려보자
(를 만나면 deck에 index를 추가
)를 만나면 deck[-1]을 확인, index의 차이가 1이면 laser이므로 pop하고, 남은 deck의 원소만큼 count 추가
index의 차이가 1이 아니면 stick이므로, pop하고 stick을 count에 추가 (count += 1)
"""

if __name__ == "__main__":
    data = input()
    deck = deque()
    count = 0
    for i in range(len(data)):
        if data[i] == "(":
            deck.append(i)
        else:
            if deck[-1] + 1 == i:
                deck.pop()
                count += len(deck)
            else:
                deck.pop()
                count += 1
    print(count)