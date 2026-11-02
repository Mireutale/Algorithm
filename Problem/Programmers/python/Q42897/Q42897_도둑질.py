"""
마을의 모든 집들은 동그랗게 배치되어 있음.
인접한 두 집을 털면 경보가 울림, 각 집에 있는 돈이 담긴 배열 money가 주어질 때, 도둑이 훔칠 수 있는 돈의 최댓값을 return

중요한 점은 첫번째 집을 털면 마지막 집을 털지 못한다는 점.

3개의 집 > 1 / 2 / 3 3가지 경우
4개의 집 > 1 3 / 2 4 2가지 경우
"""
from heapq import heappop, heappush

# 배열 말고 최댓값만 반환하게 해도 가능
def dp(money, n, start, end):
    dp_list = [0] * n
    dp_list[start] = money[start]
    dp_list[start + 1] = max(dp_list[start], money[start + 1])
    for i in range(start + 2, end):
        dp_list[i] = max(dp_list[i-1], dp_list[i-2] + money[i])
    return dp_list
        
def solution(money):
    answer = 0
    # 마을에 집이 3개인 경우
    n = len(money)
    if n == 3:
        return max(money)
    # 마을에 집이 4개 이상인 경우
    # dp[i]는 i번째 까지의 집을 털었을 때 최댓값 및 마지막에 턴 집의 위치
    # 단, 원형이므로 첫 집을 제외한 경우와(1, n-1), 마지막 집을 제외한 경우로 나눠서 dp(0, n-2)
    dp_not_first = dp(money, n, 0, n-1)
    dp_not_last = dp(money, n, 1, n)
    answer = max(dp_not_last[-1], dp_not_first[-2])
    return answer

# ---------------------------------------------------------------------------
def rob_range(money, start, end):
    prev2 = 0
    prev1 = 0

    for i in range(start, end):
        current = max(prev1, prev2 + money[i])
        prev2 = prev1
        prev1 = current

    return prev1


def solution(money):
    n = len(money)
    without_last = rob_range(money, 0, n - 1)
    without_first = rob_range(money, 1, n)
    return max(without_last, without_first)