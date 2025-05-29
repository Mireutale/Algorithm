"""
* Codes\starcoin\26532_Acres.py
* Author : mireutale

TODO 
[설계]
m, n크기의 야드로 넓이가 주어짐
acres는 4840야드넓이
1개의 옥수수 씨앗 주머니로는 5acres에 옥수수 밭을 생성 가능
"""

import sys
input = lambda: sys.stdin.readline().rstrip()
import math

if __name__ == "__main__":
    m, n = map(int, input().split())
    acres = (m * n) / 4840
    print(math.ceil(acres / 5))