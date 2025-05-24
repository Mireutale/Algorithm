import sys
input = lambda: sys.stdin.readline().rstrip()

#숫자의 개수
n = int(input())
#입력받은 숫자들
numbers = input()
#총 합
numbers_sum = 0

#i를 사용 숫자를 하나씩 분리해서 합을 구한다.
for i in range(n):
    numbers_sum += int(numbers[i])
#결과 출력
print(numbers_sum)