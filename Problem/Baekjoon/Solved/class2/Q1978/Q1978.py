import sys
import math
input = lambda: sys.stdin.readline().rstrip()

#에라스토테네스의 체
def prime_nums():
    #1000이하의 자연수이므로 1000개의 수 선택
    prime = [1 for _ in range(1001)]
    #1은 제외
    prime[1] = 0
    #i는 2부터 1000의 제곱근 까지만 수행
    #제곱근 이상의 수는 1000을 나눌수 없다.
    for i in range(2, int(math.sqrt(1000) + 1)):
        #만약 값이 True인 경우
        if prime[i] == 1:
            j = 2
            #i는 소수가 되고 i의 배수는 전부 제외한다.
            while i * j <= 1000:
                prime[i*j] = 0
                j += 1
    return prime

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    prime = prime_nums()
    result = 0
    for i in nums:
        if prime[i] == 1:
            result += 1
    print(result)


