#input을 빠르게 받기 위한 sys 라이브러리 사용
import sys
input = lambda: sys.stdin.readline().rstrip()

"""
[설계]
5섯 참가자들 중 가장 많은 점수를 얻은 사람의 번호와 사람을 출력
항상 우승자의 번호가 유일
"""

if __name__ == "__main__":
    input_data = []
    max_point = 0
    max_number = 0
    for _ in range(5):
        input_data.append(list(map(int, input().split())))
    for i in range(5):
        if max_point < sum(input_data[i]):
            max_point = sum(input_data[i])
            max_number = i + 1
    print(max_number, max_point)