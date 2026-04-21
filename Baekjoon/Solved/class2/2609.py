import sys

input = lambda:sys.stdin.readline().rstrip()

if __name__ == "__main__":
    """
    [설계]
    두개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램
    최대 공약수 -> 작은 수 부터 시작 -1씩 감소하면서 찾기
    최소 공배수 -> 더 낮은 수부터 시작 만약 만나면 종료
    시간초과
    유클리드 호제법 사용 필요
    2개의 자연수 a,b에 대해서 a를 b로 나눈 나머지를 r이라고 하면
    a와 b의 최대 공약수는 b와 r의 최대 공약수와 동일하다.
    이를 반복 -> 계속해서 나누다가 나머지가 0이 되었을 때의 수가 최대공약수
    최소 공배수 -> a와 b의 곱을 최대 공약수로 나누면 나온다.
    """
    nums = list(map(int, input().split()))

    #최대 공약수
    a = max(nums)
    b = min(nums)
    while b > 0:
        a, b = b, a % b
    gcd = a
    print(gcd)

    #최소 공배수
    print(int(max(nums) * min(nums) / gcd))