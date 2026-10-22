"""
삼각형의 꼭대기에서 바닥까지 이어지는 경로 중, 거쳐간 숫자의 합이 가장 큰 경우
아래 칸으로 이동할 때는, 대각선 방향으로 한칸 오른쪽 또는 왼쪽만 가능(i > i또는 i+1)

삼각형의 정보가 담긴 배열 triangle이 매개변수로 주어질 때, 거쳐간 숫자의 최댓값을 return
"""
def solution(triangle):
    answer = 0
    N = len(triangle)
    dp = [[0] * (num + 1) for num in range(N)]
    dp[0][0] = triangle[0][0] # 첫번째 값은 고정
    for i in range(1, N):
        for j in range(i):
            # 이전 데이터와 비교해서 가능한 값을 추가
            # 단, 다른 경로로 더하기가 추가된 값이 있는 경우는, 최댓값만 저장
            dp[i][j] = max(dp[i-1][j] + triangle[i][j], dp[i][j])
            dp[i][j+1] = max(dp[i-1][j] + triangle[i][j+1], dp[i][j+1])
    return max(dp[-1])

# ---------------------------------------------------------------------------------------------
def solution(triangle):
    # triangle의 마지막 열을 얕은 복사
    dp = triangle[-1][:]

    # 아래에서 부터 위로 값을 더하면서 계산하는 형태, 가장 마지막 행의 데이터는 본인이 가장 큰 값이므로 제외
    for row in range(len(triangle) - 2, -1, -1):
        # dp[col]은 가장 아랫 자리수에서 위로 올라갈 때, 가장 큰 값만 저장하는 형태임
        for col in range(len(triangle[row])):
            # 즉, dp[col]은 기존의 dp[col]과 dp[col + 1]중에서, 어떤 값과 triangle[row][col]을 더해야 가장 큰 값이 되는지 저장하는 것.
            dp[col] = triangle[row][col] + max(
                dp[col],
                dp[col + 1]
            )

    # 마지막 까지 계산하면, dp[1:]은 계산을 위해 저장한 중간 값이고, dp[0]가 모든 경로를 계산했을 때, 최댓값을 가짐
    return dp[0]