#input을 빠르게 받기 위한 sys 라이브러리 사용
import sys
input = lambda: sys.stdin.readline().rstrip()
import math
"""
[설계]

N := ⌊(n1 + 1)(n2 + 1)/(n12 + 1) - 1⌋
내림 정수 -> math의 floor
올림 정수 -> math의 ceil
기본 내장함수 -> 사사오입 round
사사오입원칙 -> 반올림할 자리의 수가 5인경우 앞자리의 수가 짝수면 내림, 홀수면 올림
"""

if __name__ == "__main__":
    n1, n2, n12 = map(int, input().split())
    print(math.floor((n1+1)*(n2+1)/(n12+1) - 1))