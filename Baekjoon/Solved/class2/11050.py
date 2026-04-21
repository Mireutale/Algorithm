#input을 빠르게 받기 위한 sys 라이브러리 사용
import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    """
    [설계]
    자연수 N과 정수 K가 주어진 경우 이항계수를 구하는 프로그램

    이항계수
    n C k 
    = n! / k! (n-k)! 

    시간제한 1초, 메모리 제한 256MB

    파스칼의 삼각형을 사용하면 이항 계수를 구하는게 쉬움.
    """
    n, k = map(int, input().split())
    #구하고자 하는 값 만큼 파스칼의 삼각형 크기 설정
    dp=[[1]*(n+1) for _ in range(n+1)]
    for i in range(2, n+1):
        for j in range(1, i):
            dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
    print(dp[n][k])