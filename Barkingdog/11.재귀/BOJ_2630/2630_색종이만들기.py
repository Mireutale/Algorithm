"""
* CodingTest/Barkingdog/11(0x0B).재귀/BOJ_2630/2630_색종이만들기.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def find_paper(row: int, col: int, line: int):
    compare = paper[row][col]
    for i in range(row, row+line):
        for j in range(col, col+line):
            if compare != paper[i][j]:
                for x in range(2):
                    for y in range(2):
                        find_paper(row + (line//2)*x, col + (line//2)*y, line//2)
                return
    paper_cnt[compare] += 1

if __name__ == "__main__":
    paper_cnt = { 
                    0:0,
                    1:0 
                }
    n = int(input()) # 한 변의 길이 N
    paper = [list(map(int, input().split())) for i in range(n)] # N * N 크기의 종이
    find_paper(0, 0, n)
    print(paper_cnt[0])
    print(paper_cnt[1])