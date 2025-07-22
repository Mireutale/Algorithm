"""
* CodingTest/Barkingdog/11(0x0B).재귀/BOJ_1992/192_쿼드트리.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def quad_tree(row, col, line):
    compare = video[row][col]
    for i in range(row, row+line):
        for j in range(col, col+line):
            if video[i][j] != compare:
                ans.append("(")
                for x in range(2):
                    for y in range(2):
                        next_line = line//2
                        quad_tree(row + (next_line) * x, col + (next_line) * y, next_line)  
                ans.append(")")
                return
    ans.append(compare)

if __name__ == "__main__":
    n = int(input())
    ans = list()
    video = [list(map(int, input())) for _ in range(n)]
    quad_tree(0, 0, n)
    print(*ans, sep="")