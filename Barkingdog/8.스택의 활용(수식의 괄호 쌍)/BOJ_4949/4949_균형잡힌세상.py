"""
* CodingTest/Barkingdog/8.스택의 활용(수식의 괄호 쌍)/BOJ_4949/4949_균형잡힌세상.py
* Author : mireutale
"""
import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

"""
[설계]
괄호는 소괄호("()")와 대괄호("[]") 2종류
왼쪽 괄호와 오른쪽 괄호가 짝을 이루어야 함.
문자열은 마지막 글자 제외 영문 알파벳, 공백, 소괄호, 대괄호로 이루어지며
온점(.)으로 끝나고 길이는 100글자보다 작거나 같음.

입력의 종료조건 = 온점 하나 입력(.)

덱에 소괄호 또는 대괄호의 시작 부호를 append
소괄호 또는 대괄호의 끝 부호를 만났을 때, deck의 마지막 값이
알맞은 괄호의 시작 부호이면 pop
아니면 밸런스가 맞지 않으므로 break 후 no를 출력
! 덱이 비어있지 않은 경우, 모든 짝이 맞지 않음 -> 이 경우도 no
"""

if __name__ == "__main__":
    while True:
        deck = deque()
        string = input()
        if string:
            balance = True
            if string == ".":
                break
            else:
                for word in string:
                    if word == "(" or word == "[":
                        deck.append(word)
                    if word == ")":
                        if deck and deck[-1] == "(":
                            deck.pop()
                        else:
                            balance = False
                            break
                    if word == "]":
                        if deck and deck[-1] == "[":
                            deck.pop()
                        else:
                            balance = False
                            break
                if len(deck) == 0 and balance:
                    print("yes")
                else:
                    print("no")