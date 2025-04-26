#input을 빠르게 받기 위한 sys 라이브러리 사용
import sys
input = lambda: sys.stdin.readline().rstrip()
import math
"""
[설계]
정사각형 n개를 가진 경우 -> 정사각형을 이용해서 만들 수 있는 직사각형의 개수는 몇개인가?

직사각형 A, B가 있는 경우 A를 회전, 이동시켜서 B를 만들 수 없으면 두 직사각형은 다름
직사각형을 만들 때, 정사각형을 변형시키거나, 한 정사각형 위에 다른 정사각형을 놓을 수 없다.
직사각형은 정사각형으로 꽉 차있어야 함.

n (1 ~ 10,000)
"""

if __name__ == "__main__":
    number = int(input())
    count = 0
    #좌변의 길이를 늘려가면서 n/2의 under bound까지
    for i in range(1, math.ceil(number/2)+1):
        for j in range(i, number + 1):
            if j * i > number:
                break
            else:
                count += 1
    print(count)