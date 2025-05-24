"""
* Barkingdog\0x03 배열\BOJ_2577\2577_숫자의개수.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    """
    [설계]
    
    A*B*C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇번 쓰였는지 구하는 프로그램
    
    계산 결과를 문자열로 변경하고 문자로 바꾼 값을 앞에서 하나씩 추적하면서 배열에 입력
    """

    a = int(input())
    b = int(input())
    c = int(input())

    finds_numbers = str(a*b*c)
    numbers = [0] * 10
    for i in range(len(finds_numbers)):
        numbers[int(finds_numbers[i])] += 1

    for j in range(len(numbers)):
        print(numbers[j])