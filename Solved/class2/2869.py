#input을 빠르게 받기 위한 sys 라이브러리 사용
import sys
import math
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    """
    [설계]
    1. while문 사용 -> 시간초과
    2. 시간초과를 줄이려면 -> V <= A + N*(A-B)이 성립하면 됨
    이러면 총 일은 1 + N으로 해결
    올라가야 할 높이 -> V - B 
    """

    A, B, V = map(int, input().split())
    N = 0
    days_up_height = V - B
    oneday_up_height = A - B
    up_days = days_up_height / oneday_up_height
    print(math.ceil(up_days))