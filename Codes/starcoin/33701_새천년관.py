#input을 빠르게 받기 위한 sys 라이브러리 사용
import sys
input = lambda: sys.stdin.readline().rstrip()

"""
[설계]
건물이름짓기
조건 1. 이름은 알파벳 소문자로만
조건 2. 이름의 맨 앞글자와 맨 뒤 글자는 같은 글자
조건 3. 이름에 k 와 u가 포함
조건 4. 이름의 마지막 4글자는 gwan
조건 5. 이름의 길이가 50보다 짧거나 같아야 한다

조건을 만족하는 이름을 출력
"""

if __name__ == "__main__":
    print("nkugwan")