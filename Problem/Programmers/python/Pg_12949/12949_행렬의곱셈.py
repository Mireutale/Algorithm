# PG 12949 행렬의 곱셈

import json
import sys
input = lambda: sys.stdin.readline().rstrip()

def solution(arr1, arr2):
    k, m, n = len(arr1[0]), len(arr1), len(arr2[0])
    answer = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            temp = 0
            for l in range(k):
                temp += arr1[i][l] * arr2[l][j]
            answer[i][j] = temp
    return answer

if __name__ == "__main__":
    arr1 = json.loads(input())
    arr2 = json.loads(input())
    print(solution(arr1, arr2))