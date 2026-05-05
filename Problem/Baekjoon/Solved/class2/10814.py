#input을 빠르게 받기 위한 sys 라이브러리 사용
import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    """
    [설계]
    사람들의 나이와 이름이 가입한 순서대로 주어짐

    회원들을 나이가 증가하는 순으로(오름차순), 
    나이가 같으면 먼저 가입한 사람이 앞에 오는 순서대로 정렬

    회원의 수 1 <= N <= 100,000
    나이는 1~200
    이름은 길이가 100이하

    시간 제한 3초, 메모리 제한 256MB

    ! 딕셔너리를 사용하려고 했으나, 중복되는 이름이나 나이가 있으면 value값만 바뀌고 추가가 안되는 문제
    ? 리스트를 활용 튜플로 값을 입력, 중복되는 값을 받고 lambda를 활용해서 age만 사용해서 sort를 수행
    ? 추가적으로 list에 값 입력시 age를 int로 넣어야 문자열 비교를 수행해서 값이 이상해지지 않음!
    * 파이썬은 문자여도 sort가 되는데 이유가 뭐지..? -> 문자열 비교는 숫자의 크기로 비교를 하는 것이 아니라, 자릿수에서의 문자 순서대로 비교를 수행
    * 2 > 10 이 성립해서 정렬이 잘못되는 문제!
    * int정렬시 1, 2, 5, 10, 25 / str 정렬시 1, 10, 2, 25, 5 순서로 정렬됨
    """
    N = int(input())
    users = []
    for _ in range(N):
        age, name = input().split()
        users.append((int(age), name))
    sorted_users = sorted(users, key = lambda item:item[0])
    for age, name in sorted_users:
         print(age, name)