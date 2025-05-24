"""
* Barkingdog\0x08 스택의 활용(수식의 괄호 쌍)\BOJ_2504\2504_괄호의값.py
* Author : mireutale
"""
import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

"""
[설계]
올바른 괄호열 -> () []형태
() = 2
[] = 3
(x) = 2 * x
[x] = 3 * x로 계산
두개의 올바른 괄호열 x,y가 있을때, xy = x + y의 값과 동일

예를 들어 ‘(()[[]])([])’ 의 괄호값을 구해보자.
‘()[[]]’ 의 괄호값이 2 + 3*3=11 이므로 ‘(()[[]])’의 괄호값은 2*11=22 이다. 
그리고 ‘([])’의 값은 2*3=6 이므로 전체 괄호열의 값은 22 + 6 = 28 이다.

temp를 사용해서 값을 저장 -> 시작 괄호마다 temp에 값을 곱함
시작 괄호 다음에 닫힌 괄호가 나오는 경우 -> result에 temp추가
닫힌괄호 -> deck에서 시작 괄호 제거하고 temp를 나눠줌

!예외
시작 괄호만 계속해서 나오는 경우 방지 -> 무조건 덱이 비어있어야 정답
"""

if __name__ == "__main__":
    data = input()
    deck = deque()
    temp = 1
    result = 0
    is_good = True
    for i in range(len(data)):
        if data[i] == '(':
            deck.append(data[i])
            temp *= 2
        elif data[i] == '[':
            deck.append(data[i])
            temp *= 3
        elif data[i] == ')':
            if not deck or deck[-1] != '(':
                is_good = False
                break
            # 이전 괄호가 여는 괄호인 경우 -> 값 추가
            if data[i - 1] == '(':
                result += temp
            deck.pop()
            temp //= 2
        elif data[i] == ']':
            if not deck or deck[-1] != '[':
                is_good = False
                break
            # 이전 괄호가 여는 괄호인 경우 -> 값 추가
            if data[i - 1] == '[':
                result += temp
            deck.pop()
            temp //= 3
    if not deck and is_good:
        print(result)
    else:
        print(0)
