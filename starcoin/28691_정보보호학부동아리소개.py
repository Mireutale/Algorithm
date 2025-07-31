"""
* Codes\starcoin\28691_정보보호학부동아리소개.py
* Author : mireutale

TODO 
[설계]
조건에 맞는 동아리 이름 출력
"""
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