#input을 빠르게 받기 위한 sys 라이브러리 사용
import sys
input = lambda: sys.stdin.readline().rstrip()

"""
sys.stdin.readline()을 사용해서 input보다 더 빠르게 값을 입력받음
rstrip()을 사용해서 마지막 개행문자 '\n'을 입력받지 않도록 설정
lambda함수를 사용해서 input을 sys.stdin.readline().rstrip()으로 대체
[설계]


"""

if __name__ == "__main__":
    pass