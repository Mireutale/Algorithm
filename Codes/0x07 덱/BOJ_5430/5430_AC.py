#input을 빠르게 받기 위한 sys 라이브러리 사용
import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

"""
[설계]
두 가지 함수
R : 배열에 있는 수의 순서를 뒤집는 함수

D : 첫 번째 수를 버리는 함수, 배열이 비어있는 경우 사용시 에러발생

함수는 조합해서 사용가능 ex(RDD) -> R, D, D 순서대로 수행과 동일

테스트 케이스 개수 t (1 ~ 100)

각 테스트 케이스
수행할 함수 p(1 ~ 100,000)
배열에 들어있는 수의 개수 n(0 ~ 100,000)
배열에 들어있는 정수(x1, x2 ... xn, 1 ~ 100)
"""

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        p = input()
        n = int(input())
        deck = deque(i for i in input().strip("[]").split(",") if i.isdigit())
        deck_reversed = False
        is_error = False
        for i in range(len(p)):
            # R인 경우
            if p[i] == "R":
                deck_reversed = not deck_reversed
            else:
                if deck:
                    if deck_reversed:
                        deck.pop()
                    else:
                        deck.popleft()
                else:
                    print("error")
                    is_error = True
                    break
        if not is_error:
            if deck: 
                if deck_reversed:
                    deck.reverse()
                    print(f"[{','.join(deck)}]")    
                else:
                    print(f"[{','.join(deck)}]")
            #! n의 범위도 확인해야 함!
            if len(deck) == 0:
                print("[]")