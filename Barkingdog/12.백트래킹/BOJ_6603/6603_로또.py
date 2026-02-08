# Barkingdog/12.백트래킹/BOJ_6603/6603_로또.py

import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def rotto():
    if len(deck) == 6:
        temp = tuple(deck)
        if temp not in ans:
            print(*temp)
            ans.add(temp)
            return
    
    for i in s:
        if not deck or deck[-1] < i:
            deck.append(i)
            rotto()
            deck.pop()

if __name__ == "__main__":
    while True:
        data = input().split()
        if data[0] == "0":
            break
        else:
            k = int(data[0])
            s = list(map(int, data[1:]))
            ans = set()
            deck = deque()
            rotto()
        print()
