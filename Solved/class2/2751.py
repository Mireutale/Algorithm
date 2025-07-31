#input을 빠르게 받기 위한 sys 라이브러리 사용
import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    """
    [설계]
    수의 개수 N (1 ~ 1,000,000)
    이후, 수가 주어짐 이 수는 절댓값이 1,000,000보다 작거나 같은 정수.
    수의 중복은 없음.
    
    N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력.

    내장함수 sort, sorted를 사용해도 풀리나, sys의 readline을 사용하지 않는 경우
    개행문자 "\n"을 지우는 과정이 오래 걸려서 문제를 해결하지 못할 수 있음.

    퀵 정렬이나 합병정렬을 사용해도 문제는 해결됨.
    """
    N = int(input())
    num_list = []
    for _ in range(N):
        num_list.append(int(input()))
    result = sorted(num_list)
    for i in range(N):
        print(result[i])