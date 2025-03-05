#input을 빠르게 받기 위한 sys 라이브러리 사용
import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    """
    [설계]
    알파벳 소문자로만 이루어진 단어 S

    각 알파벳이 단어에 몇 개가 포함되어 있는지 구하기

    26개의 알파벳, 아스키코드에 순서대로 입력되어 있으므로 아스키코드 사용해서 분리

    ord 문자 -> 숫자
    chr 숫자 -> 문자자
    """

    alpabet = [0] * 26
    word = input()

    for i in word:
        alpabet[ord(i) - ord('a')] += 1

    print(*alpabet)