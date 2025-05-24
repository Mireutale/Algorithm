"""
* Barkingdog\0x08 스택의 활용(수식의 괄호 쌍)\BOJ_9012\9012_괄호.py
* Author : mireutale
"""

import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

"""
[설계]
괄호문자열은 두개의 괄호 기호인 "(", ")"으로만 구성되어 있는 문자열
이중 주어진 문자열의 괄호가 알맞은지 확인
( )형태로 모두 구성되어 있어야 한다.
"""

if __name__ == "__main__":
    N = int(input())
    for _ in range(N):
        string = input()
        deck = deque()
        for i in string:
            if not deck:
                deck.append(i)
            else:
                if i == ")" and deck[-1] == "(":
                    deck.pop()
                elif i == "]" and deck[-1] == "[":
                    deck.pop()
                else:
                    deck.append(i)
        if len(deck) == 0:
            print("YES")
        else:
            print("NO")