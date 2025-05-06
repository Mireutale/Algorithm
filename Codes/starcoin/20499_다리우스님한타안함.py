"""
* Codes\starcoin\20499_다리우스님한타안함.py
* Author : mireutale


TODO 
[설계]
K/D/A를 보고 진짜 인지 판별해보자

K + A < D이거나, D = 0이면 가짜, 그렇지 않으면 진짜이다.
"""


import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    K, D, A = map(int, input().split("/"))
    real = True
    if D == 0:
        real = False
    elif K + A < D:
        real = False
    
    if real:
        print("gosu")
    else:
        print("hasu")