"""
* Codes/0x09 BFS/BOJ_2206/2206_벽부수고이동하기.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

if __name__ == "__main__":
    n, m, player = map(int, input().split())
    player_scale = list(map(int, input().split()))
    board = [list(input()) for _ in range(n)]
    
# commit msg
# --- 문제풀이_mireutale[25/ / ]