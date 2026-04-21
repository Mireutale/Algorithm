#input을 빠르게 받기 위한 sys 라이브러리 사용
import sys
input = lambda: sys.stdin.readline().rstrip()

def hash_num(data):
    # ord('a') = 97
    return ord(data) - 96

if __name__ == "__main__":
    """
    [설계]
    첫 줄에는 문자열의 길이 L이 들어온다.
    둘째 줄에는 영문 소문자로만 이루어진 문자열이 들어온다.
    입력으로 주어지는 문자열은 모두 알파벳 소문자로만 구성되어 있다.
    
    영문자를 해시 값으로 변경
    (각 알파벳의 번호) * (31^자릿수)를 전부 더해서 결과 출력

    ord() -> 문자를 아스키 코드로 변환
    chr() -> 아스키 코드를 문자로 변환
    """
    hash = 0
    data_length = int(input())
    data = input()
    for i in range(data_length):
        hash += (hash_num(data[i]) * (31 ** i))
    print(hash % 1234567891)
