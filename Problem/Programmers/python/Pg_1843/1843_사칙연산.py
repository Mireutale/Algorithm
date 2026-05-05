# Programmers/python/Pg_1843/1843_사칙연산.py

def solution(arr):
    # 숫자와 연산자만 따로 저장
    nums = [int(x) for x in arr[::2]]
    ops = [x for x in arr[1::2]]
    n = len(nums)
    max_dp = [[-float('inf')] * n for _ in range(n)]
    min_dp = [[float('inf')] * n for _ in range(n)]
    
    # i, i는 num[i]에서의 최대 최소값이므로, nums[i]로 설정
    for i in range(n):
        max_dp[i][i] = min_dp[i][i] = nums[i]
    
    # 구간의 길이 d
    for d in range(1, n):
        # 시작점 i
        for i in range(n-d):
            # 끝점 j
            j = i + d
            # k는 i와 j의 연산자를 돌면서, 최적의 위치를 찾음
            for k in range(i, j):
                op = ops[k] # i와 j 사이의 k번째 연산자
            
                if op == '+': # 연산자가 +인 경우
                    # 사이 연산자가 + 일때, 최댓값 + 최댓값 = 최댓값
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] + max_dp[k+1][j])
                    # 사이 연산자가 + 일때, 최솟값 + 최솟값 = 최솟값
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] + min_dp[k+1][j])
                else: # 연산자가 -인 경우
                    # 사이 연산자가 - 일때, 최댓값 - 최솟값 = 최댓값
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k+1][j])
                    # 사이 연산자가 - 일때, 최솟값 - 최댓값 = 최솟값
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] - max_dp[k+1][j])
    print(max_dp)
    print(min_dp)    
            
    return max_dp[0][n-1] # 1부터 n까지 전체 연산 중 최댓값 출력