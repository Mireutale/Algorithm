"""
숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현할 수 있는 방법 중
N 사용횟수의 최솟값을 return
"""
def solution(N, number):
    answer = 0
    # 미리 연속되는 숫자를 처리, 중복된 숫자를 무시하기 위해 조합 활용
    dp = [set() for _ in range(9)]
    
    # 최대 8번까지만 결산
    for cnt in range(1, 9):
        dp[cnt].add(int(str(N) * cnt))
        """
        괄호에 대한 처리가 필요함, 5+(5/5)를 보면 dp[0]와 dp[1]로 만들 수 있는 결과이고
        이 값이 dp[2]에 들어가는 형태임

        즉, 아래와 같은 형태로 풀어야 함
        dp[i] = dp[i-k] + (사칙연산) + dp[k] 

        그런데, 이 경우 이전 값 *10 + N의 형태로 숫자를 이어붙이는 연산은 불가능함
        따라서 미리 붙인 값을 처리해야하는 필요가 있음
        """
        # dp 연산 수행
        for left in range(cnt):
            right = cnt - left # left + right = cnt
            for x in dp[left]: # N을 j번 사용한 연산
                for y in dp[right]: # N을 i-j번 사용한 연산
                    # 두 연산을 사용해서 N을 i번 사용한 연산을 처리
                    dp[cnt].add(x + y)
                    dp[cnt].add(x * y)
                    dp[cnt].add(x - y)
                    if y != 0:
                        dp[cnt].add(x // y)
                        
        # 만약 타겟 번호가 있는 경우에는 연산 종료
        if number in dp[cnt]:
            return cnt
    return -1 # 8까지 정답이 없으면, -1