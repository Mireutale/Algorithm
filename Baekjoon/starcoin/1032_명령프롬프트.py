"""
* Codes/0x09 BFS/BOJ_2206/2206_벽부수고이동하기.py
* Author : mireutale
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    # n = int(input())
    # file_name = list()
    # for i in range(n):
    #     file_name.append(input())
    # ans = ""

    # for j in range(len(file_name[0])):
    #     char = file_name[0][j]
    #     for i in range(1, n):
    #         if file_name[i][j] != char:
    #             char = "?"
    #             break
    #     ans += char
    # print(ans)
    n = int(input())
    file_names = [input() for _ in range(n)]
    ans = []

    for chars in zip(*file_names):
        if all(c == chars[0] for c in chars):
            ans.append(chars[0])
        else:
            ans.append("?")
    print("".join(ans))