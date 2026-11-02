"""
m * n 크기의 지도
집은 (1,1)에 위치 학교의 좌표는 (m, n)
물에 잠긴 지역의 좌표를 담은 배열 puddles가 주어질 때, 최단경로의 개수를 1,000,000,007로 나눈 나머지를 return

범위를 넘어가는 경우와 웅덩이가 있는 경우를 제외하고, 오른쪽 or 아래를 선택해서 이동하면 됨
"""
def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1
    for row in range(n):
        for col in range(m):
            if row == 0 and col == 0: # 시작점만 패스
                continue

            if [col+1, row+1] in puddles:
                continue
            
            dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
    return dp[n-1][m-1] % 1_000_000_007