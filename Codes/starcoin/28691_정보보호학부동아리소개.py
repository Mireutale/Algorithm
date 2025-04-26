#input을 빠르게 받기 위한 sys 라이브러리 사용
import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    data = input()
    if data == "M":
        print("MatKor")
    elif data == "W":
        print("WiCys")
    elif data == "C":
        print("CyKor")
    elif data == "A":
        print("AlKor")
    else:
        print("$clear")