#input을 빠르게 받기 위한 sys 라이브러리 사용
import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    """
    [설계]
    i가 3의 배수이면서 5의 배수 -> FizzBuzz
    i가 3의 배수이지만 5의 배수가 아니면 -> Fizz
    i가 3의 배수가 아니지만 5의 배수가 아니면 Buzz
    i가 3, 5의 배수가 모두 아니면 i를 그대로 출력

    연속으로 출력된 세개의 문자열이 주어지는 경우, 다음에 올 문자열은?

    시간제한 0.5, 메모리 1024MB
    """
    strings = [input() for _ in range(3)]
    for i in range(3):
        #isdigit를 사용해서 문자열이 숫자로만 이루어져 있는지 확인
        if strings[2-i].isdigit():
            next = int(strings[2-i]) + i + 1
            break
    
    if next % 15 == 0:
        print("FizzBuzz")
    elif next % 3 == 0:
        print("Fizz")
    elif next % 5 == 0:
        print("Buzz")
    else:
        print(next)