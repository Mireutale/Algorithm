# Barkingdog/13.시뮬레이션/BOJ_17070/17070_파이프 옮기기 1.py

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    N = int(input())
    # 0 = 가로, 1 = 대각선, 2 = 세로
    count = [[[0] * N for _ in range(N)] for _ in range(3)]
    wall = [[] for _ in range(N)]
    for i in range(N):
        wall[i] = list(map(int, input().split()))

    count[0][0][1] = 1
    for i in range(2, N):
        if wall[0][i] != 1:
            count[0][0][i] = count[0][0][i-1]
    
    for i in range(1, N):
        for j in range(1, N):
            if wall[i][j] == 0 and wall[i-1][j] == 0 and wall[i][j-1] == 0:
                count[1][i][j] = count[0][i-1][j-1] + count[1][i-1][j-1] + count[2][i-1][j-1]
            
            if wall[i][j] == 0:
                count[0][i][j] = count[0][i][j-1] + count[1][i][j-1]
                count[2][i][j] = count[1][i-1][j] + count[2][i-1][j]
    
    print(sum(count[i][N-1][N-1] for i in range(3)))
