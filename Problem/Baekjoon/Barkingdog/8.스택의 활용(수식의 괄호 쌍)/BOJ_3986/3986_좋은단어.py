# Barkingdog/8.스택의 활용(수식의 괄호 쌍)/BOJ_3986/3986_좋은단어.py

import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

"""
[설계]
아치형 곡선을 그어 같은 글자끼리 쌍을 짓는다.
선끼리 교차하지 않으면서 각 글자를 정확히 한개의 다른 위치에 있는
글자와 짝 지을수 있다면, 좋은 단어라고 한다.

! 나쁜 단어
 /\ /\
/ / \ \
A B A B

? 좋은 단어
 /\  /\
/  \/  \
A  AB  B

홀수면 무조건 나쁜 단어
짝수인 경우, deck에 값이 없으면 담고 deck[-1]과 새로 입력된 값이
같으면 pop 아닌경우 append
for문이 다 돌았을 때 값이 남아있으면 나쁜 단어
값이 없으면 좋은 단어
"""

if __name__ == "__main__":
    N = int(input())
    good_string = 0
    for _ in range(N):
        string = input()
        # 짝수인 경우에만 확인
        if len(string) % 2 == 0:
            deck = deque()
            for i in range(len(string)):
                # 값이 없으면 추가
                if not deck:
                    deck.append(string[i])
                else:
                    # 값이 있는데, 지금과 다르면 append
                    if string[i] != deck[-1]:
                        deck.append(string[i])
                    # 값이 있는데, 지금과 같으면 pop
                    else:
                        deck.pop()
            # 마지막에 deck에 남은 값이 없으면 좋은 단어
            if len(deck) == 0:
                good_string += 1
    print(good_string)
