# Barkingdog/16.다이나믹프로그래밍/BOJ_14002/14002_가장긴증가하는부분수열4.py

import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    n = int(input())
    A = list(map(int, input().split()))
    dp = [[1, -1] for _ in range(n)]  # ? [길이, 이전 인덱스]
    for i in range(1, n):
        for j in range(i):
            # * 더 작은 수를 찾은 경우에, 현재 지정된 값 보다 크면 변경 
            if A[j] < A[i] and dp[i][0] < dp[j][0] + 1:
                dp[i][0] = dp[j][0] + 1
                dp[i][1] = j
            

    # 가장 긴 부분수열의 길이와 마지막 인덱스 찾기
    max_len = 0
    idx = -1
    for i in range(n):
        # * 가장 긴 부분수열의 길이보다 i가 더 긴 경우
        if dp[i][0] > max_len:
            max_len = dp[i][0]
            # * 마지막 인덱스 설정
            idx = i

    # * 부분수열 역추적
    ans = []
    while idx != -1:
        ans.append(A[idx])
        idx = dp[idx][1]
    ans.reverse()
    print(max_len)
    print(*ans)
