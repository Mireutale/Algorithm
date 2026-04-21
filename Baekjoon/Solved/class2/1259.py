import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
    """
    [설계]
    회문, palindrome : 역순으로 읽어도 똑같은 문자열을 의미
    이를 숫자로 표현
    입력의 마지막 줄은 0으로 주어진다.
    각 입력마다 주어진 수가 팰린드롬수이면 yes 아니면 no를 출력
    """
    while(1):
        is_palindrome = True
        nums = input()
        if nums == '0':
            break
        else:
            for i in range(len(nums)//2):
                if nums[i] != nums[len(nums)-1-i]:
                    is_palindrome = False
                    break
        if(is_palindrome):
            print("yes")
        else:
            print("no")