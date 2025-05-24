import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    """
    [설계]
    N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올때까지 
    0의 개수를 구하는 프로그램.

    시간 제한 2초, 메모리 제한 128MB

    0 <= N <= 500

    실제 팩토리얼 수를 계산하는건 불가능

    곱해서 0이 하나씩 증가하려면 10이 전체수에 곱해지면 됨.
    즉, 곱해지는 수에 5가 추가될때 마다 0도 1개씩 추가됨
    왜냐하면 2의 제곱수는 항상 5의 제곱수보다 작기 때문이다.
    (동일한 개수를 사용한 경우)
    """
    N:int = int(input())
    #num_of_five
    num_of_zero:int = 0
    if N >= 5:
        for i in range(5, N+1, 5):
            while i % 5 == 0 and i > 0:
                i /= 5
                num_of_zero += 1
    print(num_of_zero)
